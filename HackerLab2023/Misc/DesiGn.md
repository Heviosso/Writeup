# DesiGn
```
70 pts
```

## Description

```
[FR]
Pouvez-vous me sculpter ?

[EN]
Can you sculpt me ?

Author: r3s0lv3r
```
> Ce challenge est fournie avec un fichier csv (dahomeyArt.csv). En ouvrant le fichier on retouve deux colonnes *X*, *Y* avec des chiffres au niveau de chaque ligne. Ca nous à fait penser à des coordonnées des point dans un repere o,i,j.
> Nous avons alors écrit un script python pour marquer chaque point sur un graphe.

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dahomeyArt.csv')
x = df['Y']
y = df['X']
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', marker='o')
plt.title('Graphique de coordonnées X et Y')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
```
> Lorsqu'on execute ce script on remarque que les points ecrivent un message qui est le flag.

<image src=File/disign.png>
