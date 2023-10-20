# JPEG
```
70pts
```
## Description
```
[FR]

Connaissez-vous la signature d'une image jpg ?
[EN]

Do you know the signature of a jpg image?

Author: Hum4n

```
## Solution

Le défi nous présente deux fichiers : "flag.jpg.enc" et "xored.py". À première vue, en se basant uniquement sur les noms des fichiers, nous pouvons déjà avoir une idée de ce à quoi nous pouvons nous attendre, n'est-ce pas ? 😅. Nous avons un fichier image au format jpg qui a suibit une opération XOR pour obtenir l'image chiffrée. Explorons maintenant le contenu du script "xored.py"

```python
#!/usr/bin/env python3
from os import urandom
from random import randint
from pwn import xor

image = open("flag.jpg", "rb").read()
image_enc = open("flag.jpg.enc", "wb")

key = urandom(12) + bytes([randint(0, 9)])
image_enc.write(xor(image, key))
```
Nous ne nous trompons pas, il s'agit effectivement d'une opération XOR. Observons plus attentivement la ligne 9, celle qui définit la clé (key). La clé est définie en prenant de manière aléatoire 12 octets, plus un octet choisi aléatoirement entre 0 et 9 😅. Tout cela c'est juste pour compliquer le script, hein 😂. En réalité, l'information essentielle à retenir ici est que la clé a une taille de 13 octets, et rien de plus.

Maintenant, comment trouver la bonne image ? Rappelez-vous que la description du challenge disait : "Connaissez-vous la signature d'une image jpg ?". Dans ce cas, nous allons utiliser la signature d'une image jpg pour trouver notre clé. Puisque la clé a une taille de 13 octets, nous allons prendre une image jpg valide, extraire ses 13 premiers octets, qui constituent sa signature, puis les "XORer" avec les 13 premiers octets de notre image chiffrée. Cette opération nous donnera la clé. Ensuite, nous pourrons utiliser cette clé pour effectuer un XOR complet sur l'image afin d'obtenir notre Flag 😁.
```python
from pwn import xor

image = open("BossCat.jpg","rb").read()

image_enc = open("flag.jpg.enc", "rb").read()

newimage = open('newJPEG.jpg',"wb")

key = xor(image[:13],image_enc[:13])

#print(key)

newimage.write(xor(key,image_enc))
```
Remarquez ici que "BossCat.jpg" représente notre image de référence (n'importe quelle image JPG ferait l'affaire). Après l'exécution du script, nous obtenons notre image contenant le Flag 🥳 🥳 🥳..

<img src="File\FileJPEG\newJPEG.jpg">

# Flag
```
Flag: CTF_CrypT0_yOu_get_1t
