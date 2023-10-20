# 13- QR
```
200pts

```
## Description
```
Author: r3s0lv3r
```
## Solution
Le défi nous confronte à un fichier zip nommé "challenge.zip". Lorsque nous tentons d'extraire son contenu à l'aide de la commande unzip, un mot de passe est demandé. Cependant, le défi ne nous a pas fourni explicitement le mot de passe, donc nous devons le découvrir par nos propres moyens😪😪.

Heureusement, Mr John the Ripper est là pour nous aider à retrouver ce mot de passe, si cela est dans ses cordes. Pour utiliser John the Ripper, nous devons commencer par exécuter la commande suivante :

`>>>zip2john challenge.zip > hash.txt `

La commande génère un hash du fichier "challenge.zip" et le transfère dans un fichier nommé "hash.txt"

Ensuite, vous devrez exécuter la commande `>>>john hash.txt --wordlist=rockyou.txt` pour essayer de trouver le mot de passe.

Après avoir exécuté cette commande, vous obtiendrez le mot de passe : "codystoney".

Vous pourrez ensuite utiliser ce mot de passe pour extraire le fichier contenu dans l'archive.

À l'intérieur de l'archive, vous trouverez un fichier GIF :

<img src="File\kloklooooo.gif">

En observant attentivement le GIF, nous découvrons qu'il s'agit en fait d'un QR code en mouvement.

En utilisant l'outil disponible à l'adresse https://ezgif.com/split, nous pouvons reconstituer notre code QR :

<img src="File\recongif.png">

Il ne reste plus qu'à scanner le QR code et obtenir notre flag, n'est-ce pas ? 😁😁

Cependant, il y a une erreur😭😭. Les scanners de QR code semblent ne pas réussir à lire notre image😭😭. Cela pourrait être dû aux lignes blanches qui séparent les images individuelles du GIF. Il semble que ce ne soit pas la bonne approche😪.

Nous pouvons résoudre ce problème en écrivant un script qui prend le GIF et fusionne toutes ses images horizontalement. Allons-y !
```python
from PIL import Image

chemin_gif = "kloklooooo.gif"

image_gif = Image.open(chemin_gif)

largeur_frame, hauteur_frame = image_gif.size

nombre_frames = image_gif.n_frames

image_resultante = Image.new('RGB', (largeur_frame * nombre_frames, hauteur_frame))

for i in range(nombre_frames):
    image_gif.seek(i)
    image_frame = image_gif.copy()  # Copier le frame actuel
    image_resultante.paste(image_frame, (i * largeur_frame, 0))

image_resultante.save("image_fusionnee.png")

print("L'image fusionnée a été enregistrée sous le nom 'image_fusionnee.png'.")
```
<img src="File\image_fusionnee.png">

Nous disposons d'un QR code plus net. Après l'avoir scanné, nous récupérons notre Flagvons maintenant un QR code plus clair. Après l'avoir scanner nous obtenons notre Flag. 

## Flag 
```
Flag : CTF_13ur_5ubd1v1s3_f1x_qr_c0d3_gr34t!!))
```
