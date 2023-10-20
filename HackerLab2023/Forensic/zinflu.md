# 12 Zinflu 
```
500 pts
```

## Description
```
Adjoxosu, un membre de DokounXosu, met aux enchères l'un des trésors royaux qu'ils ont réussi à dérober aux gardiens des trésors.
```
## Outils utilisés
```


```
## Solution
```
Le challenge ne nous fournit pas d'artefact à utiliser. Nous sommes sûrement supposé faire de l'OSINT.
Nous avons commencer a faire de l'OSINT sur le nom : AdjoXosu.
Nous avons trouver un compte twitter: https://twitter.com/adjoxosu

```
<img src="File/adjoxosu.png">

```
Sur le profil twitter , nous avons également trouvé un lien vers une page github

```

<img src="File/stolenboss.png">

```
En fouillant dans les commits du dépôt github nous sommes tombés sur ceci
```
<img src="File/file_zip.png"> 

```
C'est de l'hexadécimal . On a pu reconnaître au début le nombre magique des fichiers zip: 50 4b 03 04 
Nous utilisons donc cyberchef pour avoir obtenir le fichier zip.

```
<img src="File/convert.png" >

```
Nous avons donc récuperer le fichier zip et avions essayer de l'ouvrir

```
<img src="File/unzip_open.png" >

L'erreur que nous rencontrons est liée au nom du fichier dans l'archive ZIP. Pour mieux comprendre ce problème, nous allons consulter Wikipedia pour en apprendre davantage sur le format ZIP. 

<img src="File/FileZinflu/wikizip.png">

Nous savons maintenant quels sont les octets spécifiques au nom du fichier. Ouvrons donc notre fichier extract_zip.zip avec Bless. Qu'observons-nous ? Nous remarquons que les octets qui définissent la taille du nom du fichier sont définis sur '08 00', ce qui signifie en hexadécimal qu'il s'agit de 8 octets, tout simplement.

<img src="File/FileZinflu/zinflu1.png">

Vérifions maintenant si le nombre d'octets du nom du fichier ZIP correspond effectivement à 08 octets :

<img src="File/FileZinflu/zinflu2.png">

En continuant d'observer le fichier avec notre éditeur Bless, nous remarquons que le nombre d'octets réservés pour le nom du fichier ZIP, "seeecret.jpg", est de 12 octets et non 8 octets, ce qui est probablement à l'origine de l'erreur lors de l'extraction du fichier.

Pour résoudre ce problème, essayons de corriger la taille du nom de fichier en définissant 12 octets comme suit : "0C 00"

<img src="File/FileZinflu/newextract.png">

Lorsque nous tentons à nouveau d'extraire le fichier avec notre version corrigée du ZIP, "newextract_zip.zip", nous obtenons l'image suivante :

<img src="File/FileZinflu/seeecret.jpg">

En utilisant un outil de stéganographie stegseek sur l'image, nous découvrons la présence d'un fichier caché :

<img src="File/FileZinflu/stegseekzinflu.png">

Maintenant, le problème majeur consiste à trouver un mot de passe pour extraire notre fichier caché. Lors de nos tentatives avec la wordlist "rockyou.txt", nous n'avons pas réussi à débloquer notre fichier.

Cependant, en examinant de plus près l'image et l'inscription qui s'y trouve ("le trésor est enfoui ici hahahahaha!"), nous réalisons que le mot de passe doit probablement être lié à la forme de l'image.

L'idée qui nous vient à l'esprit (grâce à notre expérience en CTF) est de prendre la valeur hexadécimale de chaque couleur dans un ordre précis. Pour cela, nous utilisons GIMP avec son outil "pipette de couleur".

<img src="File/FileZinflu/gimpzinflu1.png">

<img src="File/FileZinflu/gimpzinflu2.png">

Après avoir trouvé toutes les valeurs hexadécimales des couleurs et les avoir concaténées, nous obtenons la séquence suivante : `636c35636b6d35726b347464347535313632`. En la décodant, nous obtenons : `cl5ckm5rk4td4u5162`.

Nous pouvons maintenant tenter de l'utiliser comme mot de passe pour extraire le fichier caché de l'image.

<img src="File/FileZinflu/extractflagzinflu.png">

Nous obtenons ainsi notre flag : 

<img src="File/FileZinflu/flagzinflu.png">


## Flag 
```
Flag : CTF_Dude_You_are_gr3at_In_forensic_HLB2k23!
```

