# M3ssage
```
70 pts
```
## Description
```
Voici le message que j'ai reçu de l'expéditeur : 'Je voulais t'envoyer le message en intégralité, mais l'application l'a rejeté sous prétexte que mon fichier était trop volumineux.
Du coup, je l'ai réduit, mais je ne me rappelle plus comment j'avais fait.
Essaie de voir si tu peux retrouver le message initial de ton côté'.
```

## Outils utilisés
```
file
Cyberchef
```
## Solution
```
Après avoir télécharger le fichier , nous tentons d'identifier sont type avec la commande file sous linux
```
`>>> file message `

<img src="File/file.png">

```
Okay , le type du fichier est : zlib compressed data . Facile. Il suffit d'uploader le fichier dans cyberchef , et lui appliquer
l'opération zlib inflate.
Ensuite on trouve cette suite de caractère dans le texte: 4354465f7a6c69625f636f6d70726573735f646174615f616c676f726974686d6532313334
Appliquer l'operation "From Hex" et bingo!!!!
```
## Flag
```
CTF_zlib_compress_data_algorithme2134
```
