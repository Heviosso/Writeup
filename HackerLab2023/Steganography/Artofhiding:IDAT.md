# Art of hiding : IDAT
```
200pts
```
## Description
```
[FR]

L'ordre de succession dans le royaume a été bouleversé par les envahisseurs. Cette image renferme un trésor royal inestimable. Un petit troll a été envoyé par l'envahisseur: [24, 12, 16, 11, 32, 18, 4, 17, 7, 27, 15, 8, 21, 9, 5, 10, 26, 2, 14, 29, 22, 23, 3, 31, 25, 13, 30, 6, 20, 28, 19].
[EN]

The order of succession in the kingdom was disrupted by the invaders. This image contains a priceless royal treasure. A small troll was sent by the invader: [24, 12, 16, 11, 32, 18, 4, 17, 7, 27, 15, 8, 21, 9, 5, 10, 26, 2, 14, 29, 22, 23, 3, 31, 25, 13, 30, 6, 20, 28, 19].

FLAG : CTF_[A-Z.]

Author: 5c0r7

```
## Solution

Le défi nous présente une image PNG nommée "new.png". Lorsque nous essayons d'afficher cette image, nous constatons qu'elle est entièrement grise.

Le titre du challenge est "Art of hiding: IDAT". Mais qu'est-ce que les IDATs ? Les IDATs sont en réalité une partie intégrante d'une image PNG, et elles constituent les données visibles de l'image. 
Une image PNG est structurée comme indiqué dans le schéma suivant :

<img src="File\FileArtofHiding\structurePNG.png">

Comme on peut le voir sur l'image, il y a généralement plusieurs chunks IDAT dans une image. 
Dans notre cas, l'image est grise, ce qui suggère que les chunks IDATs ne sont pas correctement ordonnés.
Dans la description du challenge, il est question d'un "bouleversement de l'ordre", et une séquence de chiffres nous est fournie :
[24, 12, 16, 11, 32, 18, 4, 17, 7, 27, 15, 8, 21, 9, 5, 10, 26, 2, 14, 29, 22, 23, 3, 31, 25, 13, 30, 6, 20, 28, 19].
Cette liste représente l'ordre actuel des IDATs dans notre image.

La meilleure approche serait donc d'écrire un script qui réorganise l'ordre des IDATs pour créer une nouvelle image.

```python
import png
import struct
import zlib
nom_fichier_png = 'new.png'
nom_fichier_sortie = "Flag.png"

ordre_chunks_idat = [24, 12, 16, 11, 32, 18, 4, 17, 7, 27, 15, 8, 21, 9, 5, 10, 26, 2, 14, 29, 22, 23, 3, 31, 25, 13, 30, 6, 20, 28, 19]

ordre_chunks_idat = [indice - 2 for indice in ordre_chunks_idat]

idat_chunks = []
idat_chunks = [None] * len(ordre_chunks_idat)
with open(nom_fichier_png, 'rb') as fichier:
    lecteur_png = png.Reader(file=fichier)


    for chunk_type, chunk_data in lecteur_png.chunks():
        if chunk_type == b'IDAT':
            if len(ordre_chunks_idat) > 0:
                indice = ordre_chunks_idat.pop(0)
                taille_bloc_idat = struct.pack('!I', len(chunk_data))
                crc = zlib.crc32(chunk_type + chunk_data)
                crc = struct.pack('!I', crc)
                idat_chunks[indice] = taille_bloc_idat + chunk_type + chunk_data + crc


nouveau_contenu_png = b''.join(idat_chunks)
with open(nom_fichier_png, 'rb') as fichier:
	imagecontain = fichier.read()
nouveau_contenu_png = imagecontain[:58] + nouveau_contenu_png + imagecontain[13:]


with open(nom_fichier_sortie, 'wb') as fichier_sortie:
    fichier_sortie.write(nouveau_contenu_png)

print(f"La nouvelle image PNG a été créée avec les chunks IDAT réordonnés : {nom_fichier_sortie}")
```
On obtient ensuite une nouvelle image :

<img src="File\FileArtofHiding\Flag.png">

En examinant de plus près cette image, on remarque la présence de texte en morse, écrit en rouge sur l'image.

```
-.-. - ..-. ..--.- -.-.-- -.. ....- --... ..--.- -.-. .... ..- -. -.- .--. -. --. ..--.- ...-- ....- ... -.-- - --- .-.. ...-- .- .-. -.
```
En copiant le code morse et en le décodant, nous parvenons à obtenir notre Flag.

## Flag
```
Flag : CTF_!D47_CHUNKPNG_34SYTOL3ARN
```
