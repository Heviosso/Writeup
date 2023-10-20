# 2-Investigation
```
70 pts
```
## Description
```
Un fichier a été ouvert grâce au logiciel malveillant du challenge "Investigation 1".Pouvez-vous trouver le nom du fichier?
FLAG: CTF_[A-Za-z0-9]
```
## Outils utilisés
```
Volatility
Grep
```

## Solution
```
Lors de la résolution du challenge "Investigation 1" , nous avons pu conclure que le processus FoxitPDFReader , a eu un comportement suspect.
Il a démarré et s'est arrêté automatiquement. C'est un comportement souvent observé chez des logiciels malveillants.
FoxitPDFReader est un logiciel utilisé pour ouvrir des fichiers PDF. Le but ici es d'identifer quel fichier a été ouvert par le logicel
FoxitPDFReader.
Nous utiliserons le plugin cmdline de volatility , qui permet d'observer la commande utilisée pour lancer les processus présent dans le dump mémoire.
```
`>>> volatility -f Dump_forensic.mem --profile=Win7SP0x86  cmdline | grep -i foxitpdfreader`
<img scr="File/foxit.png">
```
En analysant la sortie du plugin cmdline , et en filtrant par le nom "foxitpdfreader" , nous pouvons remarquer que le logiciel FoxitPDFReader a été utilié pour ouvrir le fichier un-zeste-de-python.pdf
```
##Flag
```
CTF_un-zeste-de-python
```
