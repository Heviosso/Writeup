# Mission2
```
200 pts
```

## Description
```
[FR]
Une autre mission pour vous.

[EN]
Another mission for you.

Author: 5c0r7

http://ctf.hackerlab.bj:1034
```

> Le challenge nous renvoie vers une page web qui affiche un code QR et nous indique que notre mission se trouve à l'intérieur du code QR, et que nous devons la résoudre en moins de 5 secondes.

> La première chose que nous avons faite est de scanner le contenu du code QR pour voir quel type de mission nous attend.
 
<image src="File/mission1.png">

> Dans le code QR, il y avait une URL vers les règles `fcddd86006d92a0d54b3dfb8714ff12ca31eff19.txt` et une équation du second degré.

> Nous nous sommes rendus sur l'URL pour consulter les différentes règles.
> L'objectif est de lire le code QR, résoudre l'équation du second degré qu'il contient, puis envoyer le résultat via une requête POST sous un format spécifique en moins de 5 secondes. 😼

<image src="File/mission2.png">
    
> Pour résoudre ce challenge, nous avons écrit un script Python. L'élément important est d'utiliser la même session pour récupérer l'image et envoyer le résultat une fois l'équation résolue, sinon le code QR va changer à chaque fois.

```python
import requests
from bs4 import BeautifulSoup
import base64
import cv2
import numpy as np
import math


def resolve(a,b,c):
    discriminant = b**2 -4*a*c
    if discriminant < 0 :
        return "No solution."
    elif discriminant == 0:
        return f"x = {-b/(2*a):.3f}."
    else:
        return f"x1 = {(-b-math.sqrt(discriminant))/(2*a):.3f} , x2 = {(-b+math.sqrt(discriminant))/(2*a):.3f}."

with requests.Session() as s:
    url = 'http://ctf.hackerlab.bj:1034/'
    response = s.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        img_element = soup.find('img')
        img_data_base64 = img_element['src'].split(',')[1]
        img_data_bytes = base64.b64decode(img_data_base64)
        img = cv2.imdecode(np.frombuffer(img_data_bytes, dtype=np.uint8), -1)
        qr_code_detector = cv2.QRCodeDetector()
        retval, decoded_info, _, _ = qr_code_detector.detectAndDecodeMulti(img)
        if retval:
            print(f"Contenu du QR code : {decoded_info}")
            equation_info = decoded_info[0].split('. Equation : ')[1]
            print(f"Équation : {equation_info}")
            equation_parts = equation_info.split(' ')
            a, b, c = equation_parts[0],equation_parts[2],equation_parts[4]
            a = int(a.split('x')[0])
            b = int(b.split('x')[0])
            c = int(c)
            resultat = resolve(a, b, c)
            data = {'solution': resultat}
            print(f'result {data}')
            response2 = s.post(url, data=data)
            if response2.status_code == 200:
                print("Résultat envoyé avec succès !")
                print(f"Réponse du serveur : {response2.content.decode()}")
            else:
                print(f'Erreur lors de l\'envoi du résultat : Code d\'état {response2.status_code}')
        else:
            print("Aucun QR code trouvé.")
    else:
        print(f'Erreur : Code d\'état {response.status_code}')

```
> En exécutant ce script, nous obtenons le flag.

<image src="File/mission3.png">
    
# Flag
```CTF_QrC0d3_nO7_s3cur3_but_cod!ng_alvv@y5_fuuuuuuuun``` 😎
