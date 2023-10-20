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
