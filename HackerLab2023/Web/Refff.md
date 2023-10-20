# Refff 🔄
```
200 pts
```

## Description
```
[FR]
Le fonctionnement des en-têtes HTTP peut parfois être bizarre.

[EN]
The way HTTP headers work can sometimes be weird.

Author: Hum4n

http://ctf.hackerlab.bj:5006
```
> Ce challenge a été fourni avec le code source de l'application. Après avoir analysé le code, on remarque que l'objectif est d'effectuer une requête GET vers */flag* tout en satisfaisant la condition ```req.header("referer") === "FLAG{n0w_th4t5_W0rK1ng!}"```.

<image src="File/ref2.png">
  
> Cependant, lorsque nous ajoutons cet en-tête et sa valeur correspondante, une erreur 403 apparaît. 😔

<image src="File/ref3.png">
  
> Le problème réside dans la configuration du serveur nginx, où une règle renvoie un code d'erreur 403 lorsqu'on essaie d'accéder à */flag* sans avoir ajouté l'en-tête *referer* avec la valeur `https://hackerlab.bj`.

<image src="File/ref1.png">
  
> Nous devons donc fournir l'en-tête referer avec deux valeurs différentes. Après quelques recherches, nous avons trouvé un moyen de passer deux valeurs différentes à l'en-tête referer.😎 [Source](https://stackoverflow.com/questions/7237262/how-do-i-find-the-a-referring-sites-url-in-node)
  
<image src="File/ref4.png">
  
> Lorsque nous ajoutons ces en-têtes, nous obtenons le flag. 🚩

<image src="File/ref5.png">

# Flag

```CTF_DahomEy_n0u_``` 🥳
