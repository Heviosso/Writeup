# Sn4p-Sh0t 📸
```
500 pts
```

## Description

```
[FR]

Une application application pour capturer les trésors royaux.

[EN]

An app to capture royal treasures.

Author: W1z4rd

http://ctf.hackerlab.bj:3000
```

> Ce challenge nous dirige vers une application web qui permet de prendre des captures d'écran des sites dont on lui fournit l'URL, ce qui nous a fait penser à la vulnérabilité SSRF.

> Nous avons essayé d'envoyer ```file:///etc/passwd```, mais nous avons obtenu une erreur : `Requête invalide ou mal formée`.

> Nous avons ensuite tenté d'accéder à ```http://127.0.0.1```, mais nous avons reçu un message d'erreur : `Site web injoignable, indisponible ou invalide`.

> Nous nous somme dit qu'il y avait surement des filtres. Apres avoir chercher des moyens de contournement des filtres pour du SSRF nous avons trouver un article intéressant. [Source](https://systemweakness.com/ssrf-filter-bypass-5b8671d95565).

> Finalement, nous avons trouvé un payload qui nous a permis d'obtenir le flag. ```File:///http/../../flag.txt```

<image src="File/snap1.png">

# Flag
```CTF_c4ptur3_r3b1nd_dns_1l0v3_17``` 😎
