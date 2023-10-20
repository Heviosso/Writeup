# Messag_cipher
```
200pts
```
## Description
```
[FR]

Es-tu sûr d'être admin??
[EN]

Are you sure to be Admin???

FLAG : CTF_[A-Za-z0-9]

Author: 5c0r7

nc 54.37.70.250 1002 

```
## Solution
Le défi nous fournit un fichier nommé "script.py" ainsi que plusieurs instances de Netcat (netcat).

Voyons si nous pouvons comprendre le fonctionnement de ce script, qui est probablement la manière dont le serveur Netcat opère.
```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from base64 import b64decode,b64encode
import sys
FLAG = 'redacted'
def handle():
    print('Welcome rookie! Here I\'m able to encrypt what you want with AES in CBC mode.\nDon\'t try to Enter in Admin room if you aint.\nLet\'s go!!!')
    welcome = """
    Choose what you want to do dude!!!
    [1] Encrypt your message
    [2] Decrypt your message
    [3] Set yout encrypted Key
    [4] Admin Panel
    [5] Exit
    """
    message = ''
    key = ''
    iv = get_random_bytes(16)
    cipher = ''
    while True:
        print(welcome)
        choice = input('$> ')
        if choice not in list('12345'):
            print('Plz redo your choice, seems not undestanble')
        else:
            choice = int(choice)
            if choice == 1:
                t_message = input('Pleazure to encrypt what ever you want. Just tell me :')
                if not len(t_message):
                    print('You enter empty message. Plz try again!!!')
                    message = ''
                else:
                    message = t_message
                    if not len(key):
                        print('You not yet set your key')
                    else:
                        cipher = AES.new(key,AES.MODE_CBC,iv)
                        enc_message = b64encode(cipher.encrypt(pad(message.encode(),AES.block_size)))
                        print('Save your message :',enc_message.decode())
            elif choice == 2:
                if not len(message):
                    print('Message field empty')
                else:
                    print('Oh you already know your message. It\'s :',message)
            elif choice == 3:
                t_key = input('Plz enter your key in base64: ')
                try:
                    t_key = b64decode(t_key)
                    if len(t_key)!=32:
                        print('Invalid Key length(32 need) :',len(t_key))
                        key = ''
                    else:
                        key = t_key
                        print('Save your key')
                except:
                    print('Your base64 key aint valid')
                    key = ''
            elif choice == 4:
                t_iv = input('Enter the iv in base64 to Enter Admin :')
                try:
                    t_t_iv = b64decode(t_iv)
                    if t_t_iv == iv:
                        print('Hi Admin, your flag :', FLAG)
                        break
                except Exception as e:
                    print('Error while decoding your iv, You aint Admin!!!')
            elif choice == 5:
                print('Byeebyebye Rookie')
                break
if __name__ == '__main__':
    handle()
```

Ce script est vraiment long 😭😭, mais il est essentiel pour comprendre comment résoudre ce défi 😓😓.

Après avoir analysé le script, voici ce que nous avons compris : Il utilise un chiffrement AES en mode CBC avec une implémentation propre au challenge. Le serveur "nc" (Netcat) nous propose cinq options, dont trois sont particulièrement importantes.

La première option, "1", permet d'encrypter des données, mais pour l'utiliser, il est nécessaire de configurer notre propre clé de déchiffrement en utilisant l'option "3". L'option "4" permet de vérifier si vous êtes administrateur. Elle vous demande d'entrer l'IV (Vector d'Initialisation) utilisé pour chiffrer votre message précédemment. Il est important de noter que l'IV a été généré de manière aléatoire.

Maintenant que nous comprenons comment le serveur fonctionne, notre objectif est de trouver l'IV, qui est généré de manière aléatoire. Il n'est pas logique de tenter une attaque par force brute sur un IV de 16 octets 😂😂, c'est tout simplement ingérable. Il doit donc y avoir un autre moyen de le déterminer, en dehors de la force brute.

Cependant, avant de poursuivre, revoyons comment fonctionne le mode de chiffrement AES en mode CBC et à quel moment intervient l'IV :

<img src="File\FileMessage_Cipher\CBC_process.png">

Comme nous pouvons le constater, l'IV joue un rôle crucial dans le chiffrement et le déchiffrement des messages. Dans le chiffrement, l'IV est utilisé pour effectuer une opération XOR avec le message en clair avant qu'il ne soit transmis à la clé. Dans le déchiffrement, l'IV est utilisé pour effectuer une opération XOR avec le déchiffrement du message chiffré par la clé, ce qui permet d'obtenir le message en clair.

Maintenant, la question est de savoir comment nous pourrions trouver l'IV dans notre cas particulier. Notre situation est assez spéciale car elle nous permet de définir notre propre clé. Par conséquent, nous pouvons effectuer une partie du processus de déchiffrement et ainsi découvrir notre clé.

Concentrons-nous sur le processus de déchiffrement. Pour trouver notre IV à partir du processus de déchiffrement, que nous faut-il ? En fait, nous cherchons à obtenir la valeur DEC, qui est le résultat que nous obtenons lors du processus de déchiffrement avant l'opération XOR de l'IV 🤯🤯.

Peut-être qu'une image pourra mieux illustrer où se situe notre valeur DEC.

<img src="File\FileMessage_Cipher\DEC_CBC_process.png">

La position de la couleur "jaune" indique précisément où se trouve notre valeur DEC.

Maintenant, pour trouver DEC, il nous suffit de créer localement notre propre IV (myiv) et de l'utiliser pour déchiffrer notre cipher. Il est important de rappeler que notre cipher ici correspond au message chiffré par le serveur avec son propre IV (celui que nous cherchons).

Nous pouvons alors obtenir ceci :

fakeplaintext = decrypt(cipher, key, myiv)

myiv = (fakeplaintext) xor DEC
d'où DEC = fakeplaintext xor myiv

En connaissant DEC, nous pouvons trouver IV en utilisant l'autre formule : IV = plaintext xor DEC.

Voici un script qui automatise ce processus et affiche le Flag.
```python
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
```
En exécutant le script, nous parvenons à obtenir notre Flag. Finalement, ce n'était pas aussi évident que cela, n'est-ce pas ? 😭

## Flag 
```
Flag : CTF_!_l00v3_c3yptO_no_1d0nt
```
