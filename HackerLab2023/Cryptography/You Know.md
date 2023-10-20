# You Know
```
70pts
```
## Description
```
[FR]

Mon fichier PNG est chiffré.

[EN]

My PNG file is encrypt.

Author: W1z4rd
View Hint

XOR
```
## Solution
Le défi nous présente un fichier nommé "encryptfile.png". Lorsque nous tentons de l'ouvrir, une erreur survient :

<img src="File\FileYou_Know\erroryouknown.png">

Nous constatons que l'erreur indique que le fichier n'est pas un fichier PNG. En se référant à la description qui dit "Mon fichier PNG est chiffré", cela suggère que le fichier de base est un fichier PNG. Le hint "Xor" nous indique alors que le fichier "flag.png" a été chiffré en utilisant une opération XOR pour créer "encryptfile.png".

Pour résoudre ce challenge, il suffit de trouver la clé XOR utilisée pour effectuer le chiffrement, ce qui nous permettra de récupérer l'image PNG d'origine. Dans ce cas, nous allons utiliser la signature d'une image PNG pour retrouver cette clé.

En analysant l'en-tête d'un fichier PNG (les 8 premiers octets, également appelés la signature), nous pouvons extraire les informations nécessaires pour retrouver la clé. Cependant, il est important de noter que si nous utilisons les 8 premiers octets de l'en-tête, l'image obtenue en sortie ne sera pas valide. En revanche, si nous utilisons les 9 premiers octets de l'en-tête, nous obtiendrons une image valide en sortie.

Voici le script utilisé pour résoudre le challenge :
```python
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
```
Nous obtenons ainis notre image ainsi que notre flag : 

<img src="File\FileYou_Know\flag.png">

## Flag 
```
Flag :CTF_x0r_cl41r_kn0w_great_26737))8
```

