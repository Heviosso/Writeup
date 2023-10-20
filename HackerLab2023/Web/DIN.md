# DIN 🏰
```
200 pts
```

## Description
```
[FR]
Toujours des problèmes de sécurité avec le roi.

[EN]
There are always security issues with the king.

Author: unpasswd

http://ctf.hackerlab.bj:2005
```

> Le challenge nous redirige vers un site web avec un bouton "Next". En appuyant sur ce bouton, nous obtenons le message : ```Champion... Le roi a d'autres images spéciales pour toi```.

<image src="File/din1.png"> 

> Nous avons compris qu'il fallait charger d'autres images, mais comment faire ? 🤔 Nous avons décidé d'intercepter la requête avec Burp Suite.
> En examinant le jeton JWT avec l'extension *JWT Editor* de Burp Suite, nous avons repéré une variable intéressante : *picture_id*

<image src="File/din3.png"> 
  
> À ce moment-là, nous avons réalisé qu'il fallait modifier la variable picture_id pour charger d'autres images.

> Cependant, il ne suffit pas de modifier simplement le jeton JWT, il faut également que le jeton ait une signature valide pour que le serveur le prenne en compte.

> Pour signer les jetons que nous allons modifier, nous avons besoin de la clé secrète utilisée par l'application web.
 
> Nous avons décidé de faire du brute force sur le jeton avec *john* en espérant qu'il s'agisse d'un secret faible.

<image src="File/din4.png"> 
  
> Nous avons réussi à trouver la clé secrète : ```breakingfree```. Nous pouvons maintenant créer notre propre clé privée pour signer les différents jetons que nous allons modifier.

> Pour créer la clé privée, nous avons utilisé l'extension *JWT Editor* de Burp Suite, dans laquelle nous avons ajouté la clé secrète encodée en *base64*.

<image src="File/din5.png"> 

> Nous pouvons maintenant modifier la variable *picture_id* et signer le jeton. Une fois que nous modifions le jeton, nous obtenons le message : ```Champion... Tu as compris le système```.

<image src="File/din6.png">

> Nous avons compris qu'il fallait itérer la variable ```picture_id``` jusqu'à obtenir le flag. Nous avons donc décidé d'écrire un script Python pour générer 5000 jetons JWT en itérant à chaque fois la valeur de ```picture_id```.

```python
import jwt

secret_key = 'breakingfree'

with open('tokens.txt', 'w') as file:
    for picture_id in range(1, 5001):
        payload = {
            'picture_id': picture_id,
            'message': 'hackerlab2023',
            'author': 'Behanzin' 
        }
        token = jwt.encode(payload, secret_key, algorithm='HS256')

        file.write(token + '\n')

```
> Nous allons maintenant passer le fichier tokens.txt à l'option *intruder* de Burp Suite, en n'oubliant pas de modifier la position du payload.

<image src="File/din8.png">
  
<image src="File/din9.png">

> Après avoir lancé l'attaque, nous obtenons le flag avec l'id 1023.🫡

<image src="File/din10.png">

# Flag
```CTF_Bypass_jwt_token_to_IDOR_2341``` 🚀
