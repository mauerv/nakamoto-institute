#!/usr/bin/python3

#######################################
#              PART 1                 #
#######################################

from hashlib import sha256
from re import match

def binary_leading_0s(hex_str: str):
  binary_representation = bin(int(hex_str, 16))[2:].zfill(256)
  return len(binary_representation) - len(binary_representation.lstrip('0'))

def h(s: str) -> str:
  return sha256(s.encode()).hexdigest()

def valid_email(s: str) -> bool:
  return match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", s)

def is_valid(token: str, date: str, email: str, difficulty: int) -> bool:
  (v, d, e, n) = token.split(":")
  
  if v != "1": return False
  if len(d) > 6: return False
  if not valid_email(e): return False
  if len(n) > 16: return False

  return binary_leading_0s(h(token)) == difficulty


print(is_valid("1:081031:satoshin@gmx.com:b4c26b1694691666", "081031", "satoshin@gmx.com", 20))

print(is_valid("1:081031:satoshin@gmx.com:835b8121ee4da3f8", "081031", "satoshin@gmx.com", 20))