# Clef de l'Histoire
```
200pts
```
## Description
```
[FR]

Les légendes du royaume du Dahomey évoquent un message secret transmis de génération en génération, renfermant une information cruciale pour l'avenir du royaume. Ce message chiffré, retrouvé récemment, a été diffusé largement, sollicitant l'aide des experts du monde entier. Parmi ceux-ci, un descendant de Blaise affirme connaître des pistes pour la clé du chiffrement, mais garde le mystère.
[EN]

The legends of the Kingdom of Dahomey speak of a secret message passed down from generation to generation, containing crucial information for the kingdom's future. This encrypted message, recently discovered, has been widely disseminated, seeking the help of experts from around the world. Among them, a descendant of Blaise claims to know leads to the encryption key, but keeps the mystery.

Flag format CTF_[a-z]

Author : R!md0r

```
## Solution
Le défi nous confronte avec un fichier nommé 'enc.txt' ; voici son contenu :
```
PAQSEXCRVWKCSRLAQHYBVAWGKEYWFMCRKIKIQGKSEELCLHJMVEAUMVBILBVMQOAFQKPAURJWBABAQNCSBWKCQEOIYFJEZSJDDNASPITOAFWIUMLSGRCGBSJZLEYSPIJESWLMGEZOYEXOUSKYXIHQARQAJFWADVPSMTPOASYMUNVGFIPRLGWBDDLTQRBRLBGBUEMWQVREHZSCEEKSYEBEYBAMUEIOFEGLSSBMUEZGQRQLLPWARIURQZMUZHJIQSTSFXPEBBEMVSHUQHSNLWEXRRAOZGCCHDABDLLBAWCNUSEQVSVBFRMMIFWCAEADGMQSHBLAPAPGUPQNLDGAVEKSZXNAZZSADGLGEIJAMCJKHSWWDMRULZDMHTSOPIREYAAVDTPCZUSIJCMTHNARMRQNVGNMLNLGFSSTLTGQVISGQXPOBJWYXESCDWBEUCKXHRLUDMLAAWGVVNVIEETOUGVMFOBJQVRUUOJBHFHQFHSNLDMQVSHBOIGNPASOLNHPXIAAWOTTHDLQTELGLFDMFOBFEHCCLHLMJULFDIOUPBGCVOWDDIQSLXSQSRPGXEBEJWKQRNKSOEAHLFUMWAYHQJYCARSVVUUQAJDRLGWKXRPGQWYCOOFBTULBFVCDLASCYAPGQWKAPBKQOPVIDVYIAQSCVEYBAXPEWSJBHMHXQWREQOAKRNMWMRAELBNWWRLGMKCSZSHWXRBHUPGSLFUMWAYHQJYCAOTWQEZQUILTSOUTHDHQOIQABQGNIRLSEXBAOCEMBAOCEMHECCMAHNJCZNSRLILQOIZSLPCPVIJTHBPSZHCNVHJMSEBDXICTWCMZUEWCGWQEYZWAIOYQQWOUPAWVDCLBFRMTYSLMURPHAMPEZWNWXSSWEIXCLGEWWSZOOLCZXIWRDIWFAFYBSSEMQTYSVSGNABGADNJSFVCSTOAATULAMQMRABWARIADMWTAPBWZDPWSXIXVVIKLHLOCZRCUYSLLHLHPDETOBFWLHSHAMDMNLGHCLSZSXITOKCMVQOZOZGCTYSKMWLHTAVAEKSFWWRLFQWGSAOFKHVVIEKSIKSJLDNZQQXRENIWZUEHJQGROBHEWQRLGBIATLHEWQDLJAYCMLBLIKOZW
```
Il semble s'agir d'un message chiffré. En utilisant notre puissant outil en ligne, dCode, avec l'option "reconnaître un chiffrement", nous pouvons facilement conclure que le message que nous avons a été chiffré en utilisant le chiffrement de Vigenère. De plus, dans la description, il est mentionné qu "un descendant de Blaise affirme avoir des pistes pour la clé de chiffrement", ce qui attire également notre attention.

Dans notre situation, il est essentiel de déterminer la clé de chiffrement utilisée pour déchiffrer correctement le message en notre possession. Heureusement, dCode propose une option qui nous permet de décoder automatiquement en testant plusieurs clés suggérées par l'outil. DCode évalue ensuite les résultats obtenus et place en première position celui qui semble le plus plausible. Ainsi, nous obtenons :

<img src="File\FileCledehistoire\cledelhistoire1.png">

Il est à noter que dans le message déchiffré, nous parvenons à lire une partie du message chiffré, mais la totalité n'est pas encore déchiffrée. La clé utilisée pour obtenir ce résultat presque correct est "DAHOSI".

"DAHOSI" 🤔🤔. La clé contient "AHOSI", ce qui signifie "reine" en français, si je ne me trompe pas. Étant donné que le message déchiffré n'est pas encore tout à fait correct, cela suggère que la clé n'est pas la bonne, bien qu'elle soit proche de la clé recherchée. Nous avons essayé plusieurs clés se rapprochant de "DAHOSI" pour tenter de trouver le bon décodage.

Finalement, la clé "DAHOMEYAHOSI" déchiffre clairement notre message :

<img src="File\FileCledehistoire\cledelhistoire2.png">

À l'origine, nous pensions trouver notre Flag dans le texte déchiffré, mais ce n'était pas le cas. Le Flag était en réalité une concaténation de 'CTF_' et de la clé.
## Flag
```
Flag : CTF_dahomeyahosi
```
