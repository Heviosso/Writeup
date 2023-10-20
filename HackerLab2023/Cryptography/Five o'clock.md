# Five o'clock
```
70 pts
```
## Description
```
[FR]

Vous interceptez un message secret du mystérieux groupe Djakpataglo. Il semble que les membres de ce groupe utilisent une technique de cryptage unique basée sur une sorte de déplacement de bits. Trouvez comment récupérer le message transmis pour éviter une catastrophe imminente.
[EN]

You intercept a secret message from the mysterious Djakpataglo group. It seems that the members of this group are using a unique encryption technique based on a kind of bit shifting. Find out how to retrieve the transmitted message to avoid imminent disaster.

Author: r3s0lv3r
```
## Solution

Le défi nous présente un fichier nommé "message.txt". À l'intérieur de ce fichier, nous trouvons la séquence suivante : `688ac8eb66eb29cd6c4e66ad66cd8e26cde8eb8966cc8eeb4a068e868e2d06cd6eebe6a666864626646464`.

Il semble que ce soit un type de chiffrement. Commençons comme d'habitude en utilisant l'option "reconnaître un chiffrement" (de dcode.fr) pour décoder ce message et voir ce que cela nous donne.

<img src="File\FileFiveofclock\Fiveofclock.png">

Nous allons tenter de déchiffrer notre message crypté en utilisant les suggestions de l'outil "dcode". Lorsque nous utilisons les méthodes de Chiffre ROT-47, Code ASCII, Hexadécimal (Base 16), Codage Base62 et Chiffre XOR, nous n'obtenons pas de résultat concret. Cependant, en utilisant "Décalage Circulaire Binaire", comme suggéré dans la description, nous parvenons à trouver notre Flag.

<img src="File\FileFiveofclock\decalageFiveofclock.png">

## Flag 
```
Flag : CTF_3_Incr3m3nt1nG_L3ft_R0t4ti0ns_753421###
```


