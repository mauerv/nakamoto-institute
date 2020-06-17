max = 91
pub = 5
priv = 29

# int
print("number test")
n = ord('S')
print("original: ", n)
n = (n ** pub)  % max
print("encrypted: ", n)
n = (n ** priv) % max
print("decrypted: ", n)

# string
msg = bytearray(b"SAMPLE MSG")
print("original: ", msg)

msg = [(c ** pub)  % max for c in msg]
print("encrypted: ", msg)

msg = ([chr((c ** priv) % max) for c in msg])
print("decrypted: ", ''.join(msg))


