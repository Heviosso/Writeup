# Multi
```
200pts
```
## Description
```
[FR]

Voici encore l'une des méthodes que mon conseiller utilise pour protéger mes données.
[EN]

Here is yet another method that my advisor uses to conceal my data.

Author: unpasswd

```
## Solution

Le défi nous présente un fichier : "message". Le contenu du fichier affiche des séquences hexadécimales sur chaque ligne : 
```
c1d9f50f86825a1a2302ec2449c17196
0cc175b9c0f1b6a831c399e269772661
4a8a08f09d37b73795649038408b5f33
8ce4b16b22b58894aa86c421e8759df3
e1671797c52e15f763380b45e841ec32
4b43b0aee35624cd95b910189b3dc231
d20caec3b48a1eef164cb4ca81ba2587
0cc175b9c0f1b6a831c399e269772661
92eb5ffee6ae2fec3ad71c777531578f
d03502c43d74a30b936740a9517dc4ea2b2ad7168caa0a774cefe793ce0b33e7
36a9e7f1c95b82ffb99743e0c5c4ce95d83c9a430aac59f84ef3cbfab6145068
...
```
Nous avons essayé de décoder ces séquences hexadécimales directement, mais elles ne nous donnent pas une sortie claire. Une deuxième possibilité est que ce soit des hachages. Dans un premier temps, nous pouvons essayer de les rechercher dans la base de données de CrackStation pour voir s'ils sont facilement trouvables.

<img src="File\FileMulti\multimd5.png">

CrackStation (https://crackstation.net/) nous a permis de trouver la correspondance du premier hash, qui est visiblement une lettre et est de type MD5. Essayons maintenant avec le deuxième type de hash, qui a une taille relativement plus grande que le premier.

 <img src="File\FileMulti\multisha256.png">

CrackStation a identifié ce deuxième type de hash comme étant du SHA256, et il correspond également à une lettre. Nous avons donc deux types de hachages dans le fichier (MD5 et SHA256).

Maintenant, pour trouver l'ensemble du message, nous ne pouvons certainement pas le faire manuellement avec CrackStation 😂 😂. Ce serait trop fastidieux, et il y aurait un risque d'erreur. De plus, CrackStation demande parfois la résolution de captchas.

Allez, nous allons écrire un script qui le fait en moins de deux. On y va !😁😁

```python
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
```
Résumé du code :
Tout d'abord, il initialise une liste appelée "algos" qui contient nos deux types de hachages. Ensuite, il charge le contenu de notre fichier. il parcourt chaque ligne du fichier pour déterminer s'il s'agit d'un hachage MD5 ou SHA256, en se basant uniquement sur la longueur de la ligne. Il tente ensuite de déterminer quelle lettre correspond à ce hachage en effectuant un hachage sur tous les caractères imprimables et en comparant les résultats avec la ligne actuelle du fichier. S'il trouve une correspondance, il ajoute la lettre correspondante à la variable "flag". C'est l'ensemble du processus 😁. 

Exécutons le code pour vérifier s'il fonctionne : 

 <img src="File\FileMulti\executemulti.png">

Ça marche et bingo, nous avons notre Flag 🥳🥳."

 ## Flag 
 ```
 Flag : CTF_hashage_is_a_thing_on_this_life
```
