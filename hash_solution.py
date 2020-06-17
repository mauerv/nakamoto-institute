from hashlib import md5
import random

MAGIC_PREFIX = 'nakamoto'


def md125(s: str) -> str:
    return md5(s).hexdigest()[:8]


def random_string():
    return ''.join(random.choice('0123456789abcdef') for _ in range(10))


def generate_md125_collisions() -> (str, str):
    digests = {}  # this is a map from digests -> preimages

    while True:
        # you could also just iterate instead of random generation
        preimage = MAGIC_PREFIX + random_string()
        digest = md125(preimage.encode())

        # check if we've seen this digest before (and that the preimages are different)
        if digest in digests and digests[digest] != preimage:
            return (digests[digest], preimage)
        # otherwise, record this digest -> preimage pair
        digests[digest] = preimage
