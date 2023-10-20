# Custom
```
70pts
```
## Description
```
[FR]

J'ai caché une importante information dans cette image. Je me rappelle que le mot de passe ne faisait qu'entre 6 et 7 caractères avec un même charset que celui des fonctions de hashage.
[EN]

I hid important information in this image. I remember that the password was only between 6 and 7 characters long with the same charset as that of the hash functions.

Author: 5c0r7

```
## Solution
Le défi nous propose un fichier nommé "custom.jpg". La description du défi mentionne l'existence d'un mot de passe qui utilise le même jeu de caractères que les fonctions de hachage. Le fichier est au format JPEG, et il est fait référence à un mot de passe. L'hypothèse que nous pouvons formuler est que steghide a été utilisé pour dissimuler une information en utilisant un mot de passe conforme aux spécifications précédemment définies. Allons vérifier cette hypothèse.

`>>>stegseek --seed custom.jpg`

<img src="File\FileCustom\stegseekcustom.png">

Le résultat de la commande confirme effectivement que le fichier contient des informations cachées avec l'utilisation de steghide. Pour extraire ces informations, nous devons trouver le mot de passe approprié. C'est là que les précisions sur le mot de passe entrent en jeu. Nous sommes informés que le mot de passe comporte entre 6 et 7 caractères et utilise le même ensemble de caractères que les fonctions de hachage. Nous pouvons facilement générer un dictionnaire avec la commande "crunch" qui satisfait à ces conditions. Allons-y : 

`>>> crunch 6 7 0123456789abcdef > mypassword.txt`

Une fois que nous avons généré le dictionnaire, nous pouvons l'utiliser pour tenter de décrypter notre fichier en utilisant stegseek. 

`>>>stegseek --crack custom.jpg mypassword.txt`

<img src="File\FileCustom\stegcrackcustom.png">

Le mot de passe était donc "a1bac25". Le contenu du fichier custom.jpg.out nous donne notre flag. 

## Flag 
```
Flag : CTF_cr3aTe_0vvn_d1(o_to_B3u7efO3ce_5teghiDe
```
