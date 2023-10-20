# Atinkpòn
```
200pts
```
## Description
```
[FR]

Vous avez mis la main sur un fichier énigmatique qui semble receler un précieux secret. Cependant, le fichier a été altéré de manière à masquer son contenu original. Saurez-vous percer le secret ?
[EN]

You've got your hands on an enigmatic file that seems to conceal a precious secret. However, the file has been altered in such a way as to obscure its original contents. Can you unlock the secret?

Author: r3s0lv3r
```
## Solution

Le défi nous propose un fichier "fix_me.png". Lorsque nous essayons d'afficher l'image, une erreur se produit indiquant "Format d'image non reconnu". Cela suggère que notre image a été altérée. Cependant, examinons de plus près le type de fichier dont il s'agit.

`>>>file fix_me.png`

<img src="File\FileAtinkpon\getfileatinkpon.png">

La commande nous informe que le fichier en notre possession n'est pas un fichier PNG, mais plutôt une archive au format "gzip".

Désormais que nous savons que le fichier est une archive, procédons à sa décompression 😁😁.

Pour effectuer la décompression, nous devons d'abord renommer notre fichier de "fix_me.png" à "fix_me.gz". Ensuite, nous pouvons utiliser la commande `>>>gzip -d fix_me.gz`.

<img src="File\FileAtinkpon\erreurdezippe.png">

😪😪 Encore une erreur, donc cela ne semble pas se terminer ?

Examinons de plus près notre fichier ZIP. Nous pouvons l'ouvrir avec un éditeur hexadécimal, de préférence "bless". Cependant, parfois il peut planter lorsqu'on le sollicite trop, mais il est généralement pratique.

Qu'observons-nous avec Bless ? L'erreur indique que le Flags '0x89' n'est pas pris en charge, ce qui suggère que l'en-tête du fichier gzip a été modifié. Pour résoudre ce problème, nous allons identifier le byte du Flags et le corriger à la valeur correcte. Pour ce faire, nous aurons besoin de consulter des informations sur Wikipédia.

<img src="File\FileAtinkpon\wikipediazip.png">

Un résumé de ce que Wikipédia nous dit à propos du format gzip indique que l'en-tête du format gzip a une taille de 10 octets. Ces 10 octets sont répartis de la manière suivante :

    Les deux premiers octets (1f 8b) forment le numéro magique du fichier gzip.
    Le troisième octet (08) détermine la méthode de compression.
    Le quatrième octet, que nous examinons ici, constitue le Flags de l'en-tête.
    Les octets du 5ème au 8ème forment le timestamp, indiquant la date et l'heure à laquelle le fichier a été créé.
    Le neuvième octet concerne le Flags de compression.
    Le dixième octet constitue l'ID du système.

En analysant notre fichier, le 4ème octet a été défini comme "0x89". Toutefois, en examinant l'en-tête de fichiers gzip corrects, il apparaît que le 4ème octet est souvent défini comme '00'.

Par conséquent, nous pouvons résoudre ce problème en modifiant le 4ème octet pour le fixer à '00', puis essayer à nouveau d'extraire notre archive. 

<img src="File\FileAtinkpon\dezippe.png"> 

Enfin, ça fonctionne 🥳🥳, nous obtenons donc notre drapeau.

Lors de l'extraction de l'archive gzip, nous obtenons un fichier nommé "fix_me". Cependant, après avoir exécuté la commande "file" sur ce fichier, nous constatons qu'il s'agit encore d'une archive, mais cette fois-ci au format "tar". Espérons que l'extraction se déroule sans problème cette fois-ci 😅😅.

 `>>>tar -xvf fix_me`

 <img src="File\FileAtinkpon\extract.png">

Nous avons donc d'autres fichiers à analyser, décidément 😓😓. Continuons notre exploration :

    Le fichier "home.jpeg" renferme un fichier caché qui peut être extrait avec steghide.
    Le fichier "bow_hollay.jpeg" contient des données supplémentaires après le dernier marqueur "FFD9".
    Le fichier "greddd.jpeg" renferme un message encodé en base64. Après décodage, il affiche "This is not the flag!!!!!!!!".
    Le fichier "ball.jpeg" ne semble pas contenir d'information concrète.

Concentrons-nous sur l'image "bow_hollay.jpeg". Dans les données supplémentaires de cette image, nous avons découvert un contenu assez intéressant :
```
0000111100000011111111111100000011110000
0001111000001111111111111111000001111000
0011110000011111111111111111100000111100
0011100000111114444444444111111000011100
0111100001111444444444444441111100011110
1111000011114444444444444444111100001111
1110000111144444435400004444411110000111
11100011114444465f4400000044441111000111
111000111444421675f400000004444111000111
1100011114446307211111100000444111100011
1100011144445f37111111110000444411100011
1100011144468331111111111000044411100011
110001114445f411117777111100044411100011
1000111144482111177777711100044411110001
1000111144464611177777711100044411110001
1000111144443311177777711100044411110001
100011114446e511177777711100044411110001
11000111444f4711117777111100044411100011
110001114446f6c1111111111000044411100011
1100011144446433111111110000444411100011
1100011114446e5f311111100000444111100011
1110001114444772333400000004444111000111
1110001111444424757200000044441111000111
1110000111144444330000004444411110000111
1111000011114444444444444444111100001111
0111100001111444444444444441111100011110
0011100000111114444444444111111000011100
0011110000011111111111111111100000111100
0001111000001111111111111111000001111000
0000111100000011111111111100000011110000

```

En examinant attentivement le contenu, nous pouvons remarquer la présence d'hexadécimal du côté droit. Pour l'extraire, après une observation approfondie, nous pouvons identifier une sorte de symétrie dans le texte. Par conséquent, pour extraire notre contenu hexadécimal, il est nécessaire de suivre cette symétrie.

Pour mieux expliquer, prenons l'exemple de la 7ème ligne : 1110000111144444435400004444411110000111. En suivant la symétrie, nous pouvons diviser cette ligne en deux parties : `11100001111444444354` et `00004444411110000111`. Le contenu à extraire est donc `4354`.

En appliquant le même principe, nous obtenons la séquence : "4354465f4421675f4630725f3768335f48214646336e5f476f6c64336e5f3772333424757233".

En décodant cette séquence hexadécimale, nous obtenons le drapeau.

## Flag 
```
Flag: CTF_D!g_F0r_7h3_H!FF3n_Gold3n_7r34$ur3
```

