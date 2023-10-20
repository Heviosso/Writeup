# WARMUP 1 
> 20 points
>
> Author: W1z4rd

## Solution
Nous avons là un challenge de pwn apparemment simple à résoudre. Notons qu'il n'y a pas un fichier binaire à analyser. 
Il va nous falloir donc étudier son comportement depuis l'instance s'exécutant sur la machine distante. 

Une fois connecté par netcat, on constate le programme lit l'entrée de l'utilisateur et affiche un message de bienvenue à la suite. La première idée qui nous est venue à l'esprit est d'essayer d'exploiter un probable buffer overflow. De fil à aiguille, nous avons réussi à trouver la taille idéale du payload qui est de 77 caractères 😁. C'est ainsi que nous avons obtenu le flag

<img src=File/warmup1.png >

Plutôt easy n'est ce pas ? 🤪

> Flag : CTF_574ck_overfl0w_1s_to_easy_!!
