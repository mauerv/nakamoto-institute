#!/usr/bin/python3

#######################################
#              PART 1                 #
#######################################

from hashlib import sha256
from math import ceil, log2

def h(s: str) -> str:
  return sha256(s.encode()).hexdigest()

def fetch(nodes: list, depth: int, idx: int) -> str:
  if idx < len(nodes[depth]):
    return nodes[depth][idx]
  else:
    return '\x00'

def merkleize(sentence: str) -> str:
  nodes = []
  nodes.insert(0, sentence.split())
  depth = ceil(log2(len(nodes[0])))
  
  arr = []
  for i in range(len(nodes[0])):
    arr.insert(i, h(nodes[0][i]))
  nodes.insert(1, arr)

  for d in range(depth):
    arr = []
    for i in range(0, 2**(depth - d), 2):
      l = fetch(nodes, d + 1, i)
      r = fetch(nodes, d + 1, i + 1)
      arr.insert(i, h(l + r))
    nodes.insert(d + 2, arr)

  return nodes[depth + 1][0]

print(merkleize("I love chicken!"))

# Sample
# l1 = h("I")
# l2 = h("love")
# l3 = h("chicken!")

# l12 = h(l1 + l2)
# l34 = h(l3 + '\x00')

# root = h(l12 + l34)

# print("")
# print(l1, l2, l3)
# print(l12, l34)
# print(root)

# l1   - a83dd0ccbffe39d071cc317ddf6e97f5c6b1c87af91919271f9fa140b0508c6c
# l2   - 686f746a95b6f836d7d70567c302c3f9ebb5ee0def3d1220ee9d4e9f34f5e131
# l3   - d122d720aeeec33cf6b4cb4713c263d144720bead07c3b61e6310dbaf8b21145

# l12  - d0f8471ca8203b9f81b61c2feddabbedd37b5c167b99aae15262f7d86ce2c80b
# l34  - 355774732410d0b5b8f8be83b7c53aa69ad645b72d2feafbbac27e22ef791c29

# root - ac5544f3322e06322c6740a7c428c5cf9f2f33b88a023a3aad6d7199c31cbe29


