# Vuilton
```
200pts
```
## Description
```
[FR]

Ma clé privée ne fonctionne plus. Heureusement, j'ai un expert comme vous, sinon je ne pourrais plus lire le contenu de mes fichiers.
[EN]

My private key is no longer working. Thankfully, I have an expert like you; otherwise, I wouldn't be able to access the contents of my files.

Author: unpasswd
```

## Solution 

Le défi nous présente deux fichiers, "private.pem" et "encrypted.txt". Logiquement, nous devrions utiliser la clé privée pour décrypter le fichier chiffré et ainsi obtenir notre Flag.

Cependant, il y a un problème : dans notre fichier "private.pem", il manque deux lettres au milieu de la clé. Nous avons eu l'idée de générer toutes les combinaisons possibles de deux lettres et de les substituer à la place des lettres manquantes. Ensuite, nous pourrions utiliser ces clés privées pour tenter de déchiffrer notre fichier "encrypted.txt".

Après avoir généré toutes les clés privées potentielles, nous nous sommes rendu compte que n'importe quelle combinaison de deux lettres fonctionnait pour trouver notre Flag.

Cependant, nous mettons à votre disposition le script que nous avons utilisé : 
```python
import itertools

private_key_template = """
-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDVvYpM4LPdXtMF
WKR7VjL5KfRXDWomu3IcQLbP+y2m9Xe7yfmwgeba97ltEQ6m3OvfGqC7G5D5nBkz
LrAW7siiD9WQNP9ikRw8ziQB6djjnnX6MlTx8EWUw3BHFAx890N7pfXkVngrUndu
VZmIleXD36yvdY/duu03Fsg3Rwf5qUzxa1UXWkGqILiHLe+MfMWybVMTxHcT6mPm
pxsCF99K8XHt6h8Hnf2KEC8p/YvNDjqgaxkJb+7U92QXJ2Bm+WbJ/rjig1mVk5AD
Rx0i33evekaQNWQ7I450r0xzIwH9v2w7pSeJ4oCNpBJOfYNcl9KIMr7rhdbUD2cK
B354QatxAgMBAAECggEACRCU/qgOOsSKcazp62TrTCHLT/yUuJwtJY15T1pnTBAX
phBFoZatxzI3xAxT1S/0BTISeGL9t9dW4oK/szZI7iYapCc6QEh4FIxXzri3owYp
udzj+T+L3Oh5wNr04WEldJdUFY01Ax3YDLbuyDIWxLMOFmInkgNbK4Gg58bAe+Ye
UslPtsXEmu/Hh6TYvOzlzGURXs15iPDdfTGg9ntXlAqgU1FSdyKU3g947pDN06zP
pb9xp7z7V1lHELcm8pd1lSCxQhV7OQYxJpHaZY2eW9IdN3BnIvBwP6Zoi9uC47Y5
9uCN9CzKCwWMZRtX7CbySmamXRJcGkB4whw4q3j34QKBgQDo9kRiAogwSNjuohL4
79HqqhqLm+v+b5dPd7/ofZGpv5xOI3TQFMXuGCSD0jf6lxOihL4FMaR8HH6AFeSO
ScUy7+DUKHVg/p+M9Vb8D9nvtTSEXQyOVoJOv/??7N8hsSmBZkLMfxvLA5j+wSla
oaxBPqN3VAJNfm/8XwcAUOU1oQKBgQDq4KdfY5hS1hX94j0JKFf2qnUq33L8jjSc
bTA1688lHrjTsA57To2dw0xumhU2oKcK43RxH2wogV76DZ4a02VntHGL+zDnA63u
x1y61EMeAUNyX92PwJ8XEW152ynRBhMIDM/4aTx61AYfNNEjGErKxOZEBQdxib9O
nU2dzYAD0QKBgQDO2XPIjrT8IoK0CKbN8Ks0MQvW8IBv8AerIQn+VhiTX7ZazzK2
W+uPSFKL1Yms8J4XjMPoeraxGN/dvRKuoKP/YW0BFFd84zkqAOHWeACrzfqumKxA
amHTqKwT6KgLE3JmGjWvvCEidrRPZ5XfinQXjpW4q5hL1Lt8m6fsyOdsYQKBgQCU
wpy/SbEcJgPfvP6zYh30WJnFAakuVFL2ECHMxQF5nS+qw4MojeQb26n5ExYEd1PV
DaKeUyyJqwagkSdmDiXXvO19nyal6iqrZRFSM0YfJuW09wq5FWKtlZgk6a5eeN5s
5tCBoQVxNgB6m1UqSSR1sKe2xQil3HySKgcSvykpQQKBgHjTr1ow1l35Y7ya1cq8
FSIkEj0RDXJ6fhcCyLvcq2haHEaPkpWGepKU/JmuqDkju+Arc5fYvRoESkEINlyw
ccSLPsVdi5i1q34x2f+Lr8P6sUivdb+TCJnERRAstxSE46zWbOJxX5rr8iaSfjY+
r7FI6+bZiDj7IECbDgdOYuzb
-----END PRIVATE KEY-----
"""

possible_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

combinations = itertools.product(possible_chars, repeat=2)

for i, combo in enumerate(combinations):
    new_private_key = private_key_template.replace("??", ''.join(combo))
    
    with open(f"nouvelle_cle_{i}.pem", "w") as f:
        f.write(new_private_key)
```
Ensuite nous utilisons cette commande pour extraire notre Flag : 
`>>>openssl rsautl -decrypt -in encrypted.txt -out flag.txt -inkey newprivate.pem`

## Flag 
```
Flag: CTF_repair_rsa_file_openssl_32145
```

