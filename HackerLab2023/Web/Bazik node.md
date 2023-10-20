# Bazik node
```
200 pts
```

## Description
```
[FR]
Pourras-tu bypasser les filtres ?

[EN]
Can you bypass the filters ?

Author: Hum4n

http://ctf.hackerlab.bj:5015
```

> On nous a donné ce challenge avec un fichier *main.js*. Après avoir analysé le code, on comprend qu'il s'agit d'une simple application NodeJS/Express permettant de lire un fichier spécifique envoyé en tant que paramètre GET nommé *file*.

<image src="File/node1.png">

> Cette application dispose d'un middleware qui vérifie si le corps de la requête, les en-têtes ou les paramètres de la requête contiennent la chaîne *flag*. Si tel est le cas, elle renvoie la réponse **Bien essayé mais...!**.🙃

<image src="File/node2.png">

> On se dit alors que peut-être nous pourrions encoder le nom du fichier. Cependant, le fait que la valeur soit passée à ```fs.readFileSync``` sous forme de chaîne de caractères signifie que NodeJS n'a aucune raison de décoder la chaîne ; il vérifie simplement si un fichier de ce type existe sur le système.

Nous avons donc décidé de nous pencher sur la fonction ```fs.readFileSync```.🧐 [Source](https://nodejs.org/api/fs.html#fs_fs_readfilesync_path_options)

<image src="File/node3.png">

> Le paramètre path de la fonction ```fs.readFileSync``` peut être soit une *string*, *buffer*, *url*, *integer*. Étant donné que la fonction peut prendre un objet **url**, nous pouvons facilement contourner le filtre en encodant le nom du fichier flag.

> Le problème qui se pose maintenant est que toutes les valeurs passées au paramètre file sont envoyées à `fs.readFileSync` comme une chaîne de caractères.
> Après quelques recherches, nous avons compris que nous pouvions envoyer d'autres types de valeurs à `fs.readFileSync`, par exemple `file[a]=b&file[c]=d` sera envoyé comme `{"a": "b", "c": "d"}`. L'étape suivante consiste à former un objet URL.

> Pour formé un objet url:

- ```file``` ne doit pas etre null
- ```file.origin``` doit existé
- ```file.href``` doit existé
- ```file.protocol = file:```
- ```file.hostname = ''```
- ```file.pathname``` qui va contenir le chemain vers notre flag
  
> Nous obtenons alors comme payload 😎 ```file[origin]=x&file[href]=x&file[protocol]=file:&file[hostname]=&file[pathname]=fla%2567.txt```

<image src="File/node4.png">

## Flag
```CTF_N0de_So_s1mplE_``` 🏆
