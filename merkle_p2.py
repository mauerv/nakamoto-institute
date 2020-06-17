#!/usr/bin/python3

#######################################
#              PART 2                 #
#######################################

from enum import Enum
class Side(Enum):
  LEFT = 0
  RIGHT = 1

def validate_proof(root: str, data: str, proof: [(str, Side)]) -> bool:
  hash = h(data)
  for sibling in proof:
    if sibling[1] == Side.LEFT:
      hash = h(sibling[0] + hash)
    else:
      hash = h(hash + sibling[0])
  return hash == root