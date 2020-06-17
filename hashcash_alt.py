import random
from hashlib import sha256


def sha2(s):
    return sha256(s.encode()).hexdigest()

##################################
#            PART 1              #
##################################


def binary_leading_0s(hex_str: str):
    binary_representation = bin(int(hex_str, 16))[2:].zfill(256)
    return len(binary_representation) - len(binary_representation.lstrip('0'))


def is_valid(token: str, date: str, email: str, difficulty: int) -> bool:
    t_version, t_date, t_email, t_nonce = token.split(":")
    if t_version != "1" or t_date != date or len(t_nonce) > 16:
        return False
    if binary_leading_0s(sha2(token)) < difficulty:
        return False
    return True


##################################
#            PART 2              #
##################################


def mint(date: str, email: str, difficulty: int) -> str:
    base_token = f'1:{date}:{email}:'
    while(True):
        token = base_token + '%016x' % random.randrange(16**16)
        if binary_leading_0s(sha2(token)) > difficulty:
            return token
