from hashlib import sha1

print(sha1(b"Here we go!00").hexdigest())
# '2bf6d36bf9b140c2a62c66d79f6bd578dccdc141'
print(sha1(b"Here we go!01").hexdigest())
# 'cd7810e0446a26b4a4e7c1773989050d9fe798a2' => Nope
print(sha1(b"Here we go!02").hexdigest())
# '3fbf1f91e1a212c66f65786040bb25cc91f4598b' => Nope
print(sha1(b"Here we go!03").hexdigest())
# '2ad11aff9dd50f5e8641862638db2ff8420b89b8' => Nope
print(sha1(b"Here we go!04").hexdigest())
# '173ba0b3dc1adbce286c4ba9ea62199ab659e608' => Nope
print(sha1(b"Here we go!05").hexdigest())
# '076174d1a153e87da3248278132b007cf6adb701' => Ding ding ding!