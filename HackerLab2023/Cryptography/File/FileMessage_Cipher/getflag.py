from pwn import *
from Crypto.Random import get_random_bytes
from base64 import b64decode,b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


r  = remote("54.37.70.250",1002)

r.recvuntil("$>")
r.sendline(b'3')

#set your key : take 16 random bytes and convert to base64 

key = b64encode(get_random_bytes(32))

#send the key 

r.sendline(key)

r.recvuntil("$>")

# send the your own message for encryption 
r.sendline(b'1')

message = b"AAAAAAAAAAAAAAAA"

r.sendline(message)
#get the ciphertext of your message 
ciphertext = r.recvline(keepends=False).decode().split(":")[2]

ciphertext= b64decode(ciphertext)

#définir votre propre iv 

myiv = get_random_bytes(16)


cipher = AES.new(b64decode(key),AES.MODE_CBC,myiv)

fakeplain = cipher.decrypt(ciphertext)

DEC = xor(fakeplain[:16],myiv)

#calculer l'IV

excepIV = b64encode(xor(DEC,message))

r.recvuntil("$>")

#envoyer l'IV pour obtenir le Flag 

r.sendline(b'4')

r.sendline(excepIV)

Flag = r.recvline(keepends=False).decode().split(":")[2]

print(Flag)
