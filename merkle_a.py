from hashlib import sha1

def h(s): 
  return sha1(s.encode()).hexdigest() # hashing helper function

b1 = "Block 1"
b2 = "Block 2"
b3 = "Block 3"
b4 = "Block 4"

h1 = h(b1)
h2 = h(b2)
h3 = h(b3)
h4 = h(b4)

# d1c6d4f28135f428927a1248d71984a937ee543e
h12 = h(h1 + h2)
h34 = h(h3 + h4)
root = h(h12 + h34)

print(root)
print(h12, h34)
print(h1, h2, h3, h4)
