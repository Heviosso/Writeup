# Hackerlab
```
 200pts
```
## Description
```
[FR]

Un membre des gardiens des trésors royaux a essayé d'être malin en envoyant un secret codé en utilisant le nom de la meilleure compétition de détection de talents en cybersécurité au Bénin.

Pouvez-vous décoder le message en ayant simplement le secret codé ?

Toute la nation a foi en vous

[EN]

A member of the Royal Treasure Guards tried to be clever by sending a coded secret using the name of Benin's top cybersecurity talent spotting competition.

Can you decode the message simply by having the coded secret? The whole nation has faith in you

Author: W1z4rd

```
## Solution

Le challenge nous présente un fichier : "Hackerlab.txt". Apparemment, le contenu du fichier montre la répétition des lettres "Hackerlab" sur chaque ligne.

Pour dissimuler des informations dans les fichiers texte, il est courant d'utiliser des caractères invisibles, tels que des espaces, des tabulations ou des caractères Unicode. Commençons par vérifier si le fichier contient de tels caractères invisibles.

Pour ce faire, nous pouvons ouvrir le fichier dans Visual Studio Code. Voici le contenu affiché :

<img src="File\FileHackerlab\hackerlabinvscode.png">

On peut clairement remarquer que le fichier contient des caractères non imprimables, c'est-à-dire des caractères invisibles. La procédure à suivre serait donc d'extraire ces caractères Unicode afin de voir ce que nous pouvons faire par la suite.

Cependant, prenons un instant pour nous demander pourquoi j'ai écarté les deux premières possibilités😁😁. Lorsque nous ouvrons le fichier avec un éditeur hexadécimal, de préférence Bless, nous pouvons remarquer que le fichier ne contient ni espaces ni tabulations. S'il contenait des tabulations, l'outil stegnographique "stegnow" aurait été un meilleur allié🙃🙃.

Maintenant, procédons à l'extraction de nos fameux caractères invisibles😅. Pour ce faire, nous allons utiliser le puissant outil Cyberchef. 

Une fois sur Cyberchef , importons notre fichier hackerlab.txt, ensuite nous prenons l'option escape unicode charactere , cela permttra d'échapper les caractères invisibles. 

<img src="File\FileHackerlab\escapeunicode.png">

Ensuite, nous devrons supprimer tous les "Hackerlab" présents sur chaque ligne. Pour ce faire, nous allons utiliser l'option "Expression régulière" dans la section Regex de Cyberchef. Nous pouvons préciser "[^Hackerlab]" et sélectionner "List matches" dans la section "Output format". Cela nous fournira une sortie ne contenant que les caractères Unicode.

<img src="File\FileHackerlab\regexhackerlab.png">

Les unicodes extraits : 

```
\u200C\u200D\u200C\u200C\u200C\u200C\u000D\u000A\u200D\u200D\uFEFF\u200C\u200D\u200C\u200D\u200C\u000D\u000A\u200D\u200C\u000D\u000A\u200C\uFEFF\u200C\u200D\u200C\u200C\u200C\u200D\u200D\u200C\uFEFF\u200C\u000D\u000A\u200D\u200C\u200D\u200D\u200D\u200D\u200D\uFEFF\u200C\u200D\u200C\u200C\u200D\u200C\u000D\u000A\u200C\u200C\uFEFF\u200C\u200C\u200D\u200D\u200C\u000D\u000A\u200D\u200C\u200C\uFEFF\u200C\u200D\u200D\u200C\u200C\u200C\u200D\u200D\u000D\u000A\uFEFF\u200C\u200D\u200D\u200C\u200D\u200C\u200D\u200D\uFEFF\u000D\u000A\u200C\u200C\u200D\u200D\u200C\u200C\u200D\u200D\u000D\u000A\uFEFF\u200C\u200D\u200D\u200D\u200C\u000D\u000A\u200C\u200D\u200C\uFEFF\u200C\u200D\u200D\u200C\u200D\u200D\u200C\u200C\uFEFF\u200C\u000D\u000A\u200C\u200D\u200D\u200C\u200D\u200C\u200C\uFEFF\u200C\u200D\u200D\u200C\u000D\u000A\u200C\u200C\u200D\u200C\uFEFF\u200C\u200D\u200C\u000D\u000A\u200D\u200D\u200D\u200D\u200D\uFEFF\u000D\u000A\u200C\u200D\u200D\u200C\u200C\u200C\u200D\u200C\u000D\u000A\uFEFF\u200C\u200C\u200D\u200D\u200C\u200C\u200D\u000D\u000A\u200D\uFEFF\u200C\u200C\u200D\u200D\u200C\u200D\u200C\u200D\uFEFF\u200C\u000D\u000A\u200D\u200D\u200D\u200C\u200D\u200C\u200C\uFEFF\u200C\u200D\u200C\u200D\u200D\u200D\u000D\u000A\u200D\u200D\uFEFF\u200C\u000D\u000A\u200D\u200D\u200C\u200C\u200C\u200D\u200D\uFEFF\u200C\u200D\u200D\u200D\u000D\u000A\u200C\u200D\u200C\u200C\uFEFF\u200C\u200D\u200D\u200C\u200C\u200D\u200D\u000D\u000A\u200C\uFEFF\u200C\u200D\u200D\u200C\u200D\u200D\u200D\u200D\uFEFF\u200C\u000D\u000A\u200D\u200D\u200C\u200C\u200D\u200D\u000D\u000A\u200C\uFEFF\u200C\u200D\u200C\u200D\u200D\u200D\u000D\u000A\u200D\u200D\uFEFF\u200C\u200D\u200D\u200C\u200C\u000D\u000A\u200C\u200D\u200C\uFEFF\u200C\u200C\u200D\u200D\u200C\u200C\u200D\u200D\uFEFF\u200C\u200D\u200D\u200C\u200D\u000D\u000A\u200D\u200D\u200C\uFEFF\u200C\u200C\u200D\u200D\u000D\u000A\u200C\u200C\u200C\u200D\uFEFF\u200C\u200D\u200D\u200C\u200D\u000D\u000A\u200D\u200D\u200C\uFEFF\u200C\u200C\u200C\u200C\u000D\u000A\u200D\u200C\u200D\u200C\uFEFF\u200C\u200C\u200C\u200C\u200D\u200C\u200D\u000D\u000A\u200C\u000D\u000A\u000D\u000A\u000D\u000A\u000D\u000A\u000D\u000A\u000D\u000A\u000D\u000A

```

À ce stade, tout devient de plus en plus clair, n'est-ce pas ? 😅. Nous avons identifié cinq caractères différents : "\u200C", "\u200D", "\uFEFF", "\u000A", et "\u000D". On pourrait supposer que le créateur du défi a utilisé deux de ces caractères comme représentations binaires "0" et "1". Nous pouvons décider de prendre "\u200C" comme "0" et "\u200D" comme "1". Le petit script suivant fera le boulot :

```python
from Crypto.Util.number import *

text = "\u200C\u200D\u200C\u200C\u200C\u200C\u000D\u000A\u200D\u200D\uFEFF\u200C\u200D\u200C\u200D\u200C\u000D\u000A\u200D\u200C\u000D\u000A\u200C\uFEFF\u200C\u200D\u200C\u200C\u200C\u200D\u200D\u200C\uFEFF\u200C\u000D\u000A\u200D\u200C\u200D\u200D\u200D\u200D\u200D\uFEFF\u200C\u200D\u200C\u200C\u200D\u200C\u000D\u000A\u200C\u200C\uFEFF\u200C\u200C\u200D\u200D\u200C\u000D\u000A\u200D\u200C\u200C\uFEFF\u200C\u200D\u200D\u200C\u200C\u200C\u200D\u200D\u000D\u000A\uFEFF\u200C\u200D\u200D\u200C\u200D\u200C\u200D\u200D\uFEFF\u000D\u000A\u200C\u200C\u200D\u200D\u200C\u200C\u200D\u200D\u000D\u000A\uFEFF\u200C\u200D\u200D\u200D\u200C\u000D\u000A\u200C\u200D\u200C\uFEFF\u200C\u200D\u200D\u200C\u200D\u200D\u200C\u200C\uFEFF\u200C\u000D\u000A\u200C\u200D\u200D\u200C\u200D\u200C\u200C\uFEFF\u200C\u200D\u200D\u200C\u000D\u000A\u200C\u200C\u200D\u200C\uFEFF\u200C\u200D\u200C\u000D\u000A\u200D\u200D\u200D\u200D\u200D\uFEFF\u000D\u000A\u200C\u200D\u200D\u200C\u200C\u200C\u200D\u200C\u000D\u000A\uFEFF\u200C\u200C\u200D\u200D\u200C\u200C\u200D\u000D\u000A\u200D\uFEFF\u200C\u200C\u200D\u200D\u200C\u200D\u200C\u200D\uFEFF\u200C\u000D\u000A\u200D\u200D\u200D\u200C\u200D\u200C\u200C\uFEFF\u200C\u200D\u200C\u200D\u200D\u200D\u000D\u000A\u200D\u200D\uFEFF\u200C\u000D\u000A\u200D\u200D\u200C\u200C\u200C\u200D\u200D\uFEFF\u200C\u200D\u200D\u200D\u000D\u000A\u200C\u200D\u200C\u200C\uFEFF\u200C\u200D\u200D\u200C\u200C\u200D\u200D\u000D\u000A\u200C\uFEFF\u200C\u200D\u200D\u200C\u200D\u200D\u200D\u200D\uFEFF\u200C\u000D\u000A\u200D\u200D\u200C\u200C\u200D\u200D\u000D\u000A\u200C\uFEFF\u200C\u200D\u200C\u200D\u200D\u200D\u000D\u000A\u200D\u200D\uFEFF\u200C\u200D\u200D\u200C\u200C\u000D\u000A\u200C\u200D\u200C\uFEFF\u200C\u200C\u200D\u200D\u200C\u200C\u200D\u200D\uFEFF\u200C\u200D\u200D\u200C\u200D\u000D\u000A\u200D\u200D\u200C\uFEFF\u200C\u200C\u200D\u200D\u000D\u000A\u200C\u200C\u200C\u200D\uFEFF\u200C\u200D\u200D\u200C\u200D\u000D\u000A\u200D\u200D\u200C\uFEFF\u200C\u200C\u200C\u200C\u000D\u000A\u200D\u200C\u200D\u200C\uFEFF\u200C\u200C\u200C\u200C\u200D\u200C\u200D\u000D\u000A\u200C\u000D\u000A\u000D\u000A\u000D\u000A\u000D\u000A\u000D\u000A\u000D\u000A\u000D\u000A"


text = text.replace("\u200C","0").replace("\u200D","1").replace("\u000D","").replace("\u000A","").replace("\uFEFF","")

dec = int(text,2)

print(long_to_bytes(dec).decode())

```
Exécutons le script pour voir ce qu'il en est

<img src="File\FileHackerlab\executescript.png">

Hourra ! Nous avons notre Flag 🥳🥳🥳. Alors, finalement, ce n'était pas si difficile que ça, n'est-ce pas ? 😄

## Flag 
Flag : CTF_H4ck3rl4b_b35t_ctfof_b3n1n




