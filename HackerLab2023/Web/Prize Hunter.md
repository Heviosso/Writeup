# Prize Hunter 🏆
```
200 pts
```

## Description
```
[FR]
Une relique convoitée a échappé aux gardiens royaux depuis une génération. Vos recherches pourraient-elles permettre de la découvrir ?

[EN]
A coveted relic has eluded the royal guardians for a generation. Could your research lead to its discovery ?

Author: r3s0lv3r

http://ctf.hackerlab.bj:4000
```

> Pour ce challenge, nous avons à disposition une application web avec un espace d'enregistrement et de connexion. Nous avons décidé de créer un compte et de nous connecter. Une fois connectés, un message de bienvenue personnalisé nous attendait avec notre nom et prénom. 

<image src="File/prize1.png">
  
> Nous avons choisi d'analyser les requêtes avec Burp Suite. Nous avons remarqué qu'une fois connecté, une requête GET est envoyée vers */profile* avec un jeton JWT dans l'en-tête HTTP.

<image src="File/prize2.png">

> Nous avons donc décidé de décoder ce jeton JWT avec l'outil *JWT Editor*.

<image src="File/prize3.png">
  
> La variable `sub` du jeton JWT nous a fait penser à de l'IDOR.
> Nous nous sommes dit que si nous modifions le nombre, nous pourrions accéder au compte d'un autre utilisateur.
> Cependant, pour modifier un jeton JWT, nous avons besoin de sa clé secrète afin de pouvoir en effectuer la signature par la suite. Nous avons alors utilisé John pour essayer de trouver cette clé secrète. 🔍

<image src="File/prize4.png">
  
> Une fois que nous avons trouvé la clé secrète, nous pouvons générer une clé privée pour effectuer la signature.

<image src="File/prize6.png">

> Nous avons ensuite changé la valeur de `sub` en 1, car cela devait être le premier compte.

<image src="File/prize7.png">

> Après avoir envoyé la requête, nous avons obtenu le flag ! 🚀

<image src="File/prize8.png">

# Flag
```CTF_R3v3r51nG_t0k3n_t0_unr4v3l_7h3_myst3r13s_0f_7re45ur3``` 😎
