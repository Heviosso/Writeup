#!/usr/bin/env python3
from os import urandom
from random import randint
from pwn import xor

image = open("flag.jpg", "rb").read()
image_enc = open("flag.jpg.enc", "wb")

key = urandom(12) + bytes([randint(0, 9)])
image_enc.write(xor(image, key))
