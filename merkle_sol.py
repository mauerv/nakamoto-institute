#######################################
#              PART 1                 #
#######################################

import math
from collections import deque
from hashlib import sha256

def sha2(s):
  return sha256(s.encode()).hexdigest()

def base_layer(blocks):
  layer = [sha2(block) for block in blocks]
  while math.log2(len(layer)) % 1 != 0: # pad until we have a power of 2
    layer.append(chr(0))
  return layer

def merkleize(sentence: str) -> str:
  blocks = deque(base_layer(sentence.split(" ")))
  while len(blocks) != 1:
    blocks.append(sha2(blocks.popleft() + blocks.popleft()))
  return blocks.pop()
  
#######################################
#              PART 2                 #
#######################################

from enum import Enum
class Side(Enum):
  LEFT = 0
  RIGHT = 1

def validate_proof(root: str, data: str, proof: [(str, Side)]) -> bool:
  block = sha2(data)
  for (sibling, side) in proof:
    preimage = sibling + block if side == Side.LEFT else block + sibling
    block = sha2(preimage)
  return block == root