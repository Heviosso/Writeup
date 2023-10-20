from pwn import xor

image = open("BossCat.jpg","rb").read()

image_enc = open("flag.jpg.enc", "rb").read()

newimage = open('newJPEG.jpg',"wb")

key = xor(image[:13],image_enc[:13])

print(key)

newimage.write(xor(key,image_enc))
