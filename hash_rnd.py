#!/usr/bin/python3

from hashlib import md5
import random

prefix = "nakamoto"

max_seed = 2**16
max_loop = 2**16

def md125(s: str) -> str:
    return md5(s.encode()).hexdigest()[:8]

def generate_md125_collisions() -> (str, str):
    for seed in range(max_seed):
        random.seed(seed)
        print("=========================== SEED: ", seed)

        for attempt in range(max_loop):
            s1 = "%s%0x" % (prefix, random.getrandbits(32))
            s2 = "%s%0x" % (prefix, random.getrandbits(32))

            h1 = md125(s1)
            h2 = md125(s2)
            # print(h1, h2, h1 == h2)

            if(h1 == h2):
                print("COLLISION! seed:", seed, " attempt ", attempt)
                return(s1, s2)


generate_md125_collisions()
