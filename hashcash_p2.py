#!/usr/bin/python3

##################################
#            PART 2              #
##################################

from hashlib import sha256

def binary_leading_0s(hex_str: str):
  binary_representation = bin(int(hex_str, 16))[2:].zfill(256)
  return len(binary_representation) - len(binary_representation.lstrip('0'))

def h(s: str) -> str:
  return sha256(s.encode()).hexdigest()

def mint(date: str, email: str, difficulty: int) -> str:
  prefix = "1:%s:%s:" % (date, email)
  nonce = 0
  while 1:  
    preimg = "%s%16x" % (prefix, nonce)
    if binary_leading_0s(h(preimg)) > difficulty:
      return preimg
    nonce += 1

print(mint("081031", "satoshin@gmx.com", 20))