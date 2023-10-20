from Crypto.Util.number import *

pngheader = "89504e470d0a1a0a00"

with open("encryptfile.png", "rb") as cp :
    cipher = cp.read()

key = long_to_bytes(bytes_to_long(cipher[:9]) ^  bytes_to_long(bytes.fromhex(pngheader)))

print(key)
flag = [0]*len(cipher)

for i in range(len(cipher)) :
    flag[i] = cipher[i] ^ key[i%len(key)]

with open("flag.png", "wb") as t:
    t.write(bytes(flag))
