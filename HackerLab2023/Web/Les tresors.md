# Les trésors
```
200 pts
```

## Description
```
[FR]
Les devs ont mis en place une application pour vous permettre de partager les informations sur les trésors. Mais certains devs ont la vilaine habitude de laisser des vulnérabilités sur les sites. Peux-tu trouver la vulnérabilité pour lire le fichier que tu veux ?

[EN]
The devs have created an app to allow you to share information about treasures. But some devs have a nasty habit of leaving vulnerabilities on sites. Can you find the vulnerability to read the file you want?

Author: Hum4n

http://ctf.hackerlab.bj:5025
```

> Le challenge nous a redirigés vers une application web où l'on pouvait partager des informations. Au début, nous avons pensé que le but était de voler les cookies puisque l'application était vulnérable au XSS. Cependant, cette piste n'a rien donné.
> Après avoir analysé un peu le contenu de la requête avec Burp Suite, nous avons remarqué le paramètre *submit=*.

<image src="File/tresors1.png">

> Comme l'application web était développée avec le framework Flask de Python, nous avons pensé à une SSTI.

> Nous avons donc essayé un simple payload ```{{ 7*7 }}``` pour voir la réponse de l'application.
 
<image src="File/tresors1.1.png">

> Bingo 😎, dans la réponse, on obtient *49*. Nous avons donc cherché un payload pour exécuter du code système.[Source](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/README.md#exploit-the-ssti-by-calling-ospopenread)

> Nous avons finalement trouvé ce payload  ```{{ self.__init__.__globals__.__builtins__.__import__('os').popen('id').read() }}``` , qui nous a permis d'exécuter la commande *id*.

<image src="File/tresors2.png">
  
> Ensuite, nous avons énuméré les répertoires afin de trouver le flag, que nous avons finalement trouvé à la racine : ```{{ self.__init__.__globals__.__builtins__.__import__('os').popen('ls /').read() }}```

<image src="File/tresors3.png">

> Par la suite, nous avons lu le contenu du fichier */flag.txt*. ```{{ self.__init__.__globals__.__builtins__.__import__('os').popen('cat /flag.txt').read() }}```

<image src="File/tresors4.png">

# Flag
```CTF_Yewhe_n0n_pYthon``` 🥳
