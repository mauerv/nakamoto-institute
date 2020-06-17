def respond(
        msg_type: str,
        msg_id: int,
        msg_forwarder: int,
        msg_originator: int,
        ttl: int,
        data: Union[type(None), int]):
    '''
    This is where the meat of the P2P protocol happens.
    Upon receiving a message from a peer, what does each node do?

    Args:
        msg_type (str):
                    "PING", "PONG", or "PRIME" (you can use the constants PING/PONG/PRIME)
        msg_id (int):
                    The auto-incrementing message counter for each node
            msg_forwarder (int):
                    The port of the immediate node that sent you this message
            msg_originator (int):
                    The port of the node that created the original message (for a 0 TTL point-to-point message like a PING, this will be the same as the forwarder)
            ttl (int):
                    Time-to-live; the number of hops remaining in the lifetime of this message until it should be dropped. A 0 TTL message should not be forwarded.
            data (None or int):
                    The data in the message payload. For PINGs and PONGs, this will be None. For a PRIME message, the data field will contain the prime number.

    Returns:
        Nothing
    '''
    if msg_originator == MY_PORT:
        return

    if ((msg_id, msg_originator) in RECEIVED_MESSAGES): 
      return
    else:
      RECEIVED_MESSAGES.add((msg_id, msg_originator))

    update_last_heard_from(msg_forwarder)
    if msg_forwarder != msg_originator:
      update_last_heard_from(msg_originator)

    if msg_type == PING:
      send_message_to(msg_originator, {'msg_type': PONG, 'ttl': 0, 'data': None}, False)
    
    elif msg_type == PRIME:
      if STATE["biggest_prime"] > data or ttl <= 0:
        return
      
      STATE["biggest_prime"] = data
      STATE["biggest_prime_sender"] = msg_originator

      gsp = { "msg_originator": msg_originator, "msg_type": msg_type, "ttl":  ttl - 1, "data": data }
      
      for peer in [*STATE["peers"]]:
        send_message_to(peer, gsp, True)