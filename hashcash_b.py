#!/usr/bin/python3

from hashlib import sha1

def h(s: str) -> str:
  return sha1(s.encode()).hexdigest()

prefix = "0:030626:adam@cypherspace.org:"
difficulty = 6
nonce = 0
target = "".zfill(difficulty)

while 1:  
  preimg = "%s%x" % (prefix, nonce)
  hash = h(preimg)
  # print(hash)

  if hash[:difficulty] == target:
    print("\n\nDONE!")
    print("preimg:", preimg)
    print("hash:", hash)
    break
  
  nonce += 1

# print(sha1(b"0:030626:adam@cypherspace.org:6470e06d773e05a8").hexdigest())
# '00000000c70db7389f241b8f441fcf068aead3f0'

# DONE!
# preimg: 0:030626:adam@cypherspace.org:9ad211cc
# hash: 00000000f2c813c5ad05f2a26e7dcb8b5e03a7ca

# real	33m5,607s
# user	33m5,571s
# sys	0m0,008s

