# RandomisRandom
> 70 points
>
>[FR]
>
J'ai appris que les gardiens des trésors royaux n'aiment pas le hasard.
>[EN]
>
>I learned that guardians of royal treasures do not like chance.
>
> 
> Author: 5c0r7

## Outils utilisés pour la résolution
* **Ghidra** pour la décompilation du binaire

## Fonctionnement 
```c

undefined8 main(int param_1,long param_2)

{
  size_t sVar1;
  
  if (param_1 < 2) {
    puts("[+]Usage: ./source password");
  }
  else {
    sVar1 = strlen(*(char **)(param_2 + 8));
    if (sVar1 == 0x25) {
      randomisrandom(*(undefined8 *)(param_2 + 8));
    }
    else {
      puts("Wrong password");
    }
  }
  return 0;
}
```

Le programme prend lors de son exécution un argument. Si taille de l’argument est égale à
`37`, il est envoyé comme paramètre, que nous notons `param`, à une fonction `randomisrandom`.
Sinon, la tentative échoue. Notre analyse va donc se concentrer sur la fonction
`randomisrandom`. La fonction génère un nombre aléatoire avec `rand()` et l’enregistre une
variable `var`. Pour chacun des caractères de `param`, la fonction `randomisrandom` effectue un
`xor` avec `var` et compare les retours respectivement aux valeurs de la capture ci-dessous :

```  local_a8[0] = 0x6b8b4524;
  local_a8[1] = 0x6b8b4533;
  local_a8[2] = 0x6b8b4521;
  local_a8[3] = 0x6b8b4538;
  local_98 = 0x6b8b4527;
  local_94 = 0x6b8b450b;
  local_90 = 0x6b8b4510;
  local_8c = 0x6b8b4553;
  local_88 = 0x6b8b451e;
  local_84 = 0x6b8b4534;
  local_80 = 0x6b8b4538;
  local_7c = 0x6b8b4556;
  local_78 = 0x6b8b4509;
  local_74 = 0x6b8b450e;
  local_70 = 0x6b8b4550;
  local_6c = 0x6b8b450e;
  local_68 = 0x6b8b4506;
  local_64 = 0x6b8b452b;
  local_60 = 0x6b8b450e;
  local_5c = 0x6b8b453d;
  local_58 = 0x6b8b4502;
  local_54 = 0x6b8b4538;
  local_50 = 0x6b8b4514;
  local_4c = 0x6b8b4554;
  local_48 = 0x6b8b4527;
  local_44 = 0x6b8b4509;
  local_40 = 0x6b8b4523;
  local_3c = 0x6b8b4538;
  local_38 = 0x6b8b4533;
  local_34 = 0x6b8b450e;
  local_30 = 0x6b8b452a;
  local_2c = 0x6b8b4502;
  local_28 = 0x6b8b4538;
  local_24 = 0x6b8b4529;
  local_20 = 0x6b8b4512;
  local_1c = 0x6b8b4546;
  local_18 = 0x6b8b4546;
```

## Solution
En analysant, on remarque que le générateur de nombre aléatoire `rand()`` n’a pas été initialisé
donc sa valeur de retour est prévisible. En utilisant le code ci-dessous on obtient la valeur :
**0x6b8b4567**.
```c
#include <stdlib.h>
#include <stdio.h>

int main(){
  int u;
  u=rand();
  printf("%d", u);
  return 0
}
```

Étant donné que si var ^ C[i] = L[i] alors C[i] = L[i] ^ var, le code ci-dessous nous permet d’obtenir le
flag.

```python
liste = [0x6b8b4533, 0x6b8b4521, 0x6b8b4538, 0x6b8b4527, 0x6b8b450b, 0x6b8b4510, 0x6b8b4553, 0x6b8b451e, 0x6b8b4534, 0x6b8b4538, 0x6b8b4556, 0x6b8b4509, 0x6b8b450e, 0x6b8b4550, 0x6b8b450e, 0x6b8b4506, 0x6b8b452b, 0x6b8b450e, 0x6b8b453d, 0x6b8b4502, 0x6b8b4538, 0x6b8b4514, 0x6b8b4554, 0x6b8b4527, 0x6b8b4509, 0x6b8b4523, 0x6b8b4538, 0x6b8b4533, 0x6b8b450e, 0x6b8b452a, 0x6b8b4502, 0x6b8b4538, 0x6b8b4529, 0x6b8b4512, 0x6b8b4546, 0x6b8b4546]
t = []
for i in list:
  t.apppend(chr(i ^ 0x6b8b4567))
  print(''.join(t))
```
En utilisant le code ci-dessus, on obtient la valeur : `CTF_@lw4yS_1ni7iaLiZe_s3@nD_TiMe_Nu!!`

>Flag : CTF_@lw4yS_1ni7iaLiZe_s3@nD_TiMe_Nu!!
