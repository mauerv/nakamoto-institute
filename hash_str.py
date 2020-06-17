#!/usr/bin/python3

from hashlib import md5
import random

prefix = "nakamoto"
cache = {}

def md125(s: str) -> str:
    return md5(s.encode()).hexdigest()[:8]

def generate_md125_collisions() -> (str, str):
    while 1:
        pre = "%s%0x" % (prefix, random.getrandbits(32))
        hash = md125(pre)
        # print(pre, hash)

        if hash in cache:
            if pre == cache[hash]:
                continue
            
            # print("COLLISION!:", pre, cache[hash])
            return(pre, cache[hash])
        else:
            cache[hash] = pre

generate_md125_collisions()
