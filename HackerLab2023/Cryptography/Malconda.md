# MALCONDA 
```
 200 points
```
## Description 
```
Author: unpasswd
```
## Solution
Après s'être connecté à la machine distante, on obtient deux paraphraphes de texte: 
> Hello mon sauveur... J'ai téléchargé par erreur un fichier malicieux hier soir. Tout le contenu de mon PC a été chiffré. Je ne connais même pas l'algorithme ni la clé de chiffrement. Néanmoins, j'ai vu le nom "hmzakhalid". Pourriez-vous m'aider à retrouver mes fichiers ?
>
>Voici un exemple de fichier que j'ai récupéré avant d'éteindre mon pc : gAAAAABlHBbV7MEpnek7h5igs4ZFAMUNHYmHnIwhZ7WvSAwphkEWKyY8PuZR5zbZ2euzhT0psTDe9pJ_Ny4xVKA74QIdMwkU7GXahr8Uux-YI9szl4BVL8qs8NQcINTS_SRWN7R4hw0BZF9T0dRMKxSifG7qv-S0tsxhAfc-ph6a0SySz-aH9OQ=

La première idée qui nous est venue à l'esprit d'essayer de décoder `gAAAAABlHBbV7MEpnek7h5igs4ZFAMUNHYmHnIwhZ7WvSAwphkEWKyY8PuZR5zbZ2euzhT0psTDe9pJ_Ny4xVKA74QIdMwkU7GXahr8Uux-YI9szl4BVL8qs8NQcINTS_SRWN7R4hw0BZF9T0dRMKxSifG7qv-S0tsxhAfc-ph6a0SySz-aH9OQ=`. A travers l'outil [**Reconnaitre un chiffrement**](https://www.dcode.fr/identification-chiffrement) de dcode, nous avons analysé le supposé cipher.

<img src=File/identification_cyper_malconda.png>

On a donc essayé le déchiffrement pas base64 puis par substitution. 

<img src=File/base64_decode_malconda.png>
<img src=File/substitution_malconda.png>

Un cul de sac 😔!

En relisant bien le paragraphe obtenu, un mot a retenu notre attention: **hmzakhliad**. Il s'agit peut être d'un pseudo. Nous allons essayer d'explorer la piste osint. Parmi les résultats de la recherche de `hmzakhaliad` sur google, il y avait un lien linkedin. Nous avons donc visité cette page. 

Que découvrons nous sur son profil ? `hmzakhaliad` est un développeur! Et quand on parle d'un dev à quoi pense t'on immédiatement? Ses réalisations ouvertes au public. En tout cas c'est la première chose que je vérifie moi 😅.

Donc à travers le google dorking, nous avons recherché le pseudo `hmzakhaliad` sur la plateforme d'hébergement de code github et voilà le résultat:

<img src=File/dorking_malconda.png>

Le deuxième résultat était des plus attrayants 🤩! Nous avons donc poussé notre curiosité plus loin en visitant la page. C'était le code source d'un virus polymorphique écrit en python. Comment ça marche ?

Le code commence par calculer un hash du fichier lui-même (le fichier contenant le code du virus) en utilisant SHA-1. Ce hash ne fait pas partie du code du virus, mais il est utilisé pour identifier le fichier hôte. Ensuite, le code stocke la clé `key` et le texte chiffré `token` dans le code. Ces valeurs sont utilisées pour le chiffrement et le déchiffrement du code du virus qui est stocké dans le fichier. La fonction `decrypt` est définie pour déchiffrer le code chiffré à l'aide de Fernet, puis exécuter ce code.

Le code principal du virus commence avec l'appel à la fonction run. La fonction `execute` est définie pour afficher un message (dans le code original, "Hello World") lorsqu'elle est appelée. La fonction `run` est ensuite appelée, et elle commence par extraire le code du virus stocké dans le fichier. Le code du virus est chiffré à l'aide de la clé `key` et du texte chiffré `token`. Le virus est déchiffré et stocké dans la variable `virus`. La clé `key` est ensuite régénérée, et le code du virus est chiffré à nouveau avec la nouvelle clé et stocké dans la variable `token`. Le fichier hôte est modifié pour inclure la nouvelle clé `key` et le texte chiffré `token`, puis le code du virus est exécuté. Finalement, le fichier hôte original est supprimé, et le fichier modifié est renommé pour prendre sa place. Cela permet au virus de se propager en infectant d'autres fichiers à mesure qu'ils sont exécutés. [Voir code source](https://github.com/hmzakhalid/Polymorphic-Virus-Python.git)

En gros, le programme exécute d'abord le virus "Hello World" et utilise la clé `key` et de du hash `token` dans le code pour créer un nouveau fichier virus. Grâce à la  fonction `decode`, la nouvelle version du virus affiche est exécuté et affiche le message clair chiffré avec la clé `key` dans `token`. 

Nous avons donc remplacé le token du code original par notre cypher en espérant que la clé soit la même. Après la première exécution le virus exécuté est "Hello World". Ce qui est normal. Ensuite nous avons exécuté une deuxième fois le même programme.

<img src=File/flag_malconda.png>

Et bingo ! Nous avons notre flag 😁

> Flag: CTF_hmzakhalid_hacked_my_pc_1561





