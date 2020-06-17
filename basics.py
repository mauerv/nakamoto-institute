import binascii
from hashlib import sha1

def hash(n):
  return n % (2 ** 128)

str = b"a_really_good_password"

print("sha1: ", sha1(str).hexdigest())
print("hash: ", hash(int.from_bytes(str, 'big')))

print("11111111: ", sha1(binascii.b2a_uu(b"11111111")).hexdigest())
# 'a31518892830eec9ea21762e8bb101ce13890aee'

# let's flip a single bit and see what happens
print("11011111: ", sha1(binascii.b2a_uu(b"11011111")).hexdigest())
# 'c68b4d1bb5154c76370f33895d5d9350a4c73ba9'