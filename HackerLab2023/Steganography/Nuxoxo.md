# Nuxoxo
```
200pts
```
## Description
```
[FR]

En dehors de la boîte !
[EN]

Outside the box !

Author: r3s0lv3r
```
## Solution
Le défi nous présente un fichier image intitulé "proj_.png".

Comme c'est typique pour les challenges de stéganographie, nous avons exploré différentes pistes, notamment l'utilisation de l'outil "strings", des filtres de couleur, "binwalk", "zsteg", et d'autres techniques courantes pour les images PNG. Malheureusement, aucune de ces approches n'a abouti à des résultats significatifs.

C'est à ce moment que nous nous sommes penchés sur la description du challenge, qui mentionnait "En dehors de la boîte". Cela nous a incités à réfléchir de manière plus créative, et nous avons envisagé que peut-être, la solution se trouvait à l'extérieur de l'image elle-même.

Nous n'avions pas encore exploré l'option de redimensionner l'image, et la description "Outside the box" pourrait suggérer que nous devions penser au-delà des dimensions actuelles de l'image.

Nous avons décidé de procéder manuellement en modifiant les dimensions de l'image. Pour ce faire, nous avons ouvert l'image "proj_.png" dans un éditeur hexadécimal (dans ce cas, "bless") pour identifier l'emplacement des octets définissant la taille de l'image.

Après quelques recherches sur Wikipedia, nous avons appris que la taille de l'image est spécifiée dans la section du chunk IHDR. Après les 8 premiers octets de l'en-tête, nous avons compté 8 octets supplémentaires pour arriver au 16e octet. Les 4 premiers octets, c'est-à-dire les octets 17, 18, 19 et 20, définissent la largeur de l'image, tandis que les 4 octets suivants spécifient la hauteur de l'image.

<img src="File\FileNuxoxo\sizeofproj.png">

Maintenant que nous avons identifié où nous devons intervenir, nous allons convertir la valeur 600 en hexadécimal. La représentation hexadécimale de 600 sur 4 octets donne : "00 00 02 58".

<img src="File\FileNuxoxo\newproj.png">

Essayons maintenant d'ouvrir notre image. Cependant, nous rencontrons une erreur :

<img src="File\FileNuxoxo\errorproj.png">

Comme on peut le constater sur l'image, une erreur liée au CRC du chunk IHDR est survenue, probablement due à notre modification précédente. Pour résoudre ce problème, nous allons simplement calculer le CRC du chunk IHDR et le remplacer par le CRC incorrect. Pour ce faire, nous pourrions utiliser Python pour calculer le CRC, mais pour plus de rapidité, nous allons soumettre notre image 'lettest.png' à un analyseur (https://www.nayuki.io/page/png-file-chunk-inspector). Celui-ci devrait nous fournir le bon CRC, car il détectera également l'erreur.

<img src="File\FileNuxoxo\inspector.png">

Il est nécessaire de remplacer le CRC "7C18C945" par "F10DE6FD" pour corriger l'image.

<img src="File\FileNuxoxo\correctproj.png">

Au final, nous obtenons cette image :

<img src="File\FileNuxoxo\goodone.png">

En observant attentivement l'image, nous remarquons des inscriptions en bas de celle-ci qui semblent être un message chiffré en symboles. Après une observation plus approfondie, ces symboles ressemblent au braille.

Le message encodé est le suivant : ⠞⠋_⠛⠼⠉⠝⠼⠁⠼⠚⠥⠎_⠓⠼⠙⠉⠅⠼⠉⠗_⠍⠔⠙⠖

Après décodage, nous obtenons notre Flag.
## Flag
```
Flag : CTF_G3N10US_H4CK3R_MIND!
```
