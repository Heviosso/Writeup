# Anonyme
```
70pts
```
## Description
```
[FR]

Toujours l'une des méthodes que mon conseiller utilise pour chiffrer mes données.
[EN]

Still one of the methods my advisor uses to encrypt my data.

Author: unpasswd
View Hint

l33t
```
## Solution

Le défi nous propose deux fichiers : "encrypt" et "private.key".

En utilisant la commande "file" sur le fichier "encrypt" avec la commande `>>>file encrypt`, nous découvrons qu'il s'agit d'un fichier `PGP RSA encrypted session key`. Nous pouvons donc le déchiffrer en utilisant la clé privée que nous avons. Cependant, nous devons d'abord importer la clé privée.

Nous importons la clé privée en utilisant la commande `>>>gpg --import private.key`. Nous sommes confrontés à un défi : il nous faut connaître le mot de passe nécessaire pour importer la clé privée, ce qui peut être un jeu de devinettes fastidieux.

Après avoir essayé plusieurs mots de passe sans succès, un indice est apparu dans le challenge en mentionnant "leet". Nous utilisons donc "4N0NYM0U5" comme mot de passe pour importer la clé privée.

À ce stade, nous pouvons déchiffrer facilement le fichier "encrypt" en utilisant la commande `>>>gpg -d encrypt`.

 <img src="File\FileAnonymous\anony.png"> 

 Et nous obtenons notre flag :

 ## Flag 
 ```
Flag : CTF_gpg_gnu_privacy_guard_124353
```

 

 
