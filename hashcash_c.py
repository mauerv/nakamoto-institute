#!/usr/bin/python3

from hashlib import sha1
from random import getrandbits

def h(s: str) -> str:
  return sha1(s.encode()).hexdigest()

prefix = "0:030626:adam@cypherspace.org:"
difficulty = 6
nonce = 0
target = "".zfill(difficulty)

while 1:  
  preimg = "%s%x" % (prefix, getrandbits(64))
  hash = h(preimg)
  # print(hash)

  if hash[:difficulty] == target:
    print("\n\nDONE!")
    print("preimg:", preimg)
    print("hash:", hash)
    break
  
# print(sha1(b"0:030626:adam@cypherspace.org:6470e06d773e05a8").hexdigest())
# '00000000c70db7389f241b8f441fcf068aead3f0'

