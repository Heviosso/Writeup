# Custom Encryption
> 70 points
>
>[FR]
>
>Pour rendre leur communication toujours plus sécurisée, les gardiens utilisent des techniques pleines d'innovation pour chiffrer les messages. Malheureusement, ces techniques ne sont pas toujours dignes de confiance.
>[EN]
>
>To make their communication ever more secure, guards use innovative techniques to encrypt messages. Unfortunately these techniques are not always trustworthy.
>
> 
> Author: Hum4n

## Fonctionnement 
```python
def encrypte_c(text):
    encrypted_text = ''
    key1 = 0b1101101
    key2 = 5

    for char in text:
        encrypted_char = ord(char) ^ key1
        encrypted_char = (encrypted_char << key2) | (encrypted_char >> (8 - key2))
        encrypted_char = (encrypted_char + 42) % 256
        binary_representation = bin(encrypted_char)[2:]
        binary_representation = binary_representation.zfill(8)
        inverted_binary = ''.join('1' if bit == '0' else '0' for bit in binary_representation)
        encrypted_text += inverted_binary + ' '

    return encrypted_text



'''
Fonction de chiffrement du flag.
'''

# flag.txt: 00010000 10101110 01110000 10001111 11110000 01010000 10110000 10001111 01001010 01110001 00101110 11010010 10101110 10001111 00001110 11010100 01110001 10101110
```
La fonction de chiffrement effectue une série d'opérations logiques et arithmétiques sur les caractères d'une chaine `text` entrée en paramètre. Pour chaque caractère, nous avons tout d'abord un `xor` de la correspondance unicode avec une clé `key1`. Ensuite  une union de valeurs issues d'opérations décalage à droite et à gauche respectivement de `key2` et de `8-key2` bits. Après avoir ajouté 42 au résultat obtenu, la nouvelle valeur unicode du caractère devient le reste de la division eucludienne de l'ancienne valeur par 42. Enfin, la fonction inverse les bits de sa représentation binaire sur 8bits convertie en chaine de caractères.

## Solution

Pour obtenir le flag, nous avons écrit l'algorithme inverse de la fonction `encrypte_c` sachant que A ^ B = C ==> A ^ C = B et qu'il faut utiliser un masque & 0xFF pour s'assurer que le résultat de l'inversement de l'opération de décalage soit dans la plage de 0 à 255.

```python
my_list = []
with open ("flag.txt","r") as file:
	encrypted_text = file.readline().split()
	for t in encrypted_text:
		binary = "".join("0" if bit == "1" else "1" for bit in t)
		char = int(binary, 2)
		char = (char - 42)%256
		char = ((char >> 5) | (char << 3)) & 0xff
		my_list.append(chr(char ^ 0b1101101))
	print(''.join(my_list))
```

>Flag : CTF_BAD_1NPuT_SeNT

