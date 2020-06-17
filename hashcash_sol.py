##################################
#            PART 1              #
##################################

from hashlib import sha256
import random

HASHCASH_TEMPLATE = '1:{}:{}:'

def sha2(preimage):
    return sha256(preimage.encode()).hexdigest()
    
def binary_leading_0s(hex_str: str):
    binary_representation = bin(int(hex_str, 16))[2:].zfill(256)
    return len(binary_representation) - len(binary_representation.lstrip('0'))

def is_valid(token: str, date: str, email: str, difficulty: int) -> bool:
    prefix = HASHCASH_TEMPLATE.format(date, email)
    nonce = token[len(prefix):]

    if len(date) > 6:
        return False
    elif not token.startswith(prefix):
        return False
    elif ':' in nonce:
        return False
    elif len(nonce) > 16:
        return False
    return binary_leading_0s(sha2(token)) == difficulty

##################################
#            PART 2              #
##################################

def mint(date: str, email: str, difficulty: int) -> str:
    prefix = HASHCASH_TEMPLATE.format(date, email)

    while True:
        nonce = hex(random.randint(0, 2 ** 64 - 1))[2:].zfill(16)
        token = prefix + nonce
        if binary_leading_0s(sha2(token)) == difficulty:
            return token
