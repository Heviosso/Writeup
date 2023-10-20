# MAINTENANCE
```
200 pts
```

## Description
```
[FR]
Pendant que nous travaillions sur le site officiel des trésors royaux, nous avons mis en place un site par défaut.

[EN]
While we were working on the official royal treasures website, we have put up a placeholder site.

Author: unpasswd

http://ctf.hackerlab.bj:2011
```

> Le challenge nous renvoie vers un site qui semble être en construction. Nous avons alors décidé d'utiliser *feroxbuster* pour énumérer les répertoires afin de vérifier s'il n'y a pas de divulgation d'informations.

<image src="File/maintenance1.png">

> On trouve lors de l'énumération un répertoire *.git/* nous avons alors utilisé l'outil *git dumper* pour télécharger le répertoire. [Source](https://github.com/internetwache/GitTools/tree/master/Dumper)

<image src="File/maintenance2.png">
  
> Une fois le répertoire téléchargé, on retrouve dans le fichier *config* un lien vers un autre dépôt github ```https://github.com/senku2000/l-tech.git```.

<image src="File/maintenance3.png">

> Une fois sur ce dépôt, on trouve trois branches, la branche principale *main* et deux autres *hackerlab* et *maintenance*

<image src="File/maintenance4.png">
  
> On se dirige ensuite vers la branche *hackerlab* où nous trouvons 4 commits.

<image src="File/maintenance5.png">
  
> En regardant dans les commits, on retrouve un message : ```flag: 'CTF_under_construction_213, tu es fou pourquoi tu as mis le secret ici. je déplace moi même...................'```

<image src="File/maintenance6.png">
  
> Mais il ne s'agissait pas du vrai flag. Un peu plus bas dans les commits, on retrouve une chaîne de caractères qui ressemblait à de l'hexadécimal ```4354465f3631375f3358503035313731304e5f483334443533347243485f33323137343534```

<image src="File/maintenance7.png">

> Une fois décodée, on obtient le flag.

<image src="File/maintenance8.png">

# Flag
```CTF_617_3XP051710N_H34D534rCH_3217454``` 🥳
 
