#######################################
#              PART 1                 #
#######################################

from enum import Enum
from hashlib import sha256
import math


def hash(s: str) -> str:
    return sha256(s.encode()).hexdigest()


def merkleize(sentence: str) -> str:
    tokens = sentence.split(" ")
    hashes = list(map(hash, tokens))
    while math.log2(len(hashes)) % 1 != 0:
        hashes.append('\00')
    while len(hashes) > 1:
        new_hashes = []
        for x1, x2 in zip(hashes[::2], hashes[1::2]):
            new_hashes.append(hash(x1 + x2))
        hashes = new_hashes
    return hashes[0]

#######################################
#              PART 2                 #
#######################################


class Side(Enum):
    LEFT = 0
    RIGHT = 1


def validate_proof(root: str, data: str, proof: [(str, Side)]) -> bool:
    result = hash(data)
    for h, side in proof:
        if side == Side.LEFT:
            result = hash(h + result)
        else:
            result = hash(result + h)
    return result == root
