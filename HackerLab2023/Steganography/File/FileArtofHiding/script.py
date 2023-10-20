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
