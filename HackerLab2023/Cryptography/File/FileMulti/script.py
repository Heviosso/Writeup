from Crypto.Hash import MD5, SHA256
algos = [MD5,SHA256]
import string
with open("messages", "r") as f:
    hashes = f.readlines()

flag = ""
for i in range(len(hashes)):
    if len(hashes[i]) == 33 :
        algo = algos[0]
    else :
        algo = algos[1]
    hash = hashes[i]

    for char in string.printable:
        test_hash = algo.new()
        test_hash.update(char.encode())
        if test_hash.hexdigest() == hash.strip() :
            flag += char
print(flag)
