# Ricky
```
30pts
```
## Description
```
Author: W1z4rd
```
## Solution 

Le défi nous propose un fichier nommé "encode.txt". À l'ouverture de ce fichier, nous découvrons une séquence de chiffres binaires composée de "0" et "1".

Lorsque nous affichons ce fichier et ajustons la dimension du terminal, nous pouvons observer que les chiffres binaires forment deux codes QR distincts :

<img src="File\FileRicky\rickyQR.png">

En tentant cette fois-ci de remplacer les "1" par des espaces à l'aide de la commande "sed", le code QR devient beaucoup plus lisible. À ce stade, nous pouvons scanner le code QR pour obtenir notre drapeau. Cependant, la probabilité de réussir le scan est de 1 sur 2.

<img src="File\FileRicky\rickycleanQR.png">

Nous avons également une autre approche à notre disposition en utilisant "dcode" avec son option "image-binaire" (https://www.dcode.fr/image-binaire). En copiant le contenu de notre fichier "encode.txt" dans la section "Générateur d'Image à partir de Binaire" et en ajustant la taille de l'image à '50', nous pouvons générer notre code QR sous forme d'une image au format PNG.

<img src="File\FileRicky\dcode-image.png">

Nous pouvons alors scanner le code QR pour obtenir notre Flag.

## Flag
```
Flag : CTF_qrb1n4ry
```




