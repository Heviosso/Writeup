# Pivot
```
70 pts
```
# Description
```
Wfno iuum yy fcalzfz odb qiefoi! Jwwqcmgiaqkahhn, wnu'xh ztswlupp wi! Lay wkqves lw IAN_npobrt_kzx_xemfdr_tlhirl_gwqwhdo. Cxyk vmtr ylxx hjxee lcj rk gjnb arbkq ykhanbd nkpyk! :).

Author: r3s0lv3r
```

> Ce challenge nous ai fourni avec un texte chiffré. En se referant au nom du challenge on se rend rapidement compte qu'il s'agit du chiffrement de viginère.
> Apres avoir essayé de le decoder en ligne avec plusieurs outils sans succes nous avons décider d'écrire un code python pour le decoder.

```python
def dechiffrer_vigenere(message_chiffre, cle):
    message_dechiffre = ""
    cle_repeated = (cle * (len(message_chiffre) // len(cle))) + cle[:len(message_chiffre) % len(cle)]
    for i in range(len(message_chiffre)):
        if message_chiffre[i].isalpha():
            decalage_message = ord(message_chiffre[i].upper()) - ord('A')
            decalage_cle = ord(cle_repeated[i].upper()) - ord('A')
            lettre_dechiffree = chr(((decalage_message - decalage_cle) % 26) + ord('A'))
            if message_chiffre[i].islower():
                lettre_dechiffree = lettre_dechiffree.lower()
            message_dechiffre += lettre_dechiffree
        else:
            message_dechiffre += message_chiffre[i]
    return message_dechiffre

message_chiffre = "Wfno iuum yy fcalzfz odb qiefoi! Jwwqcmgiaqkahhn, wnu'xh ztswlupp wi! Lay wkqves lw IAN_npobrt_kzx_xemfdr_tlhirl_gwqwhdo. Cxyk vmtr ylxx hjxee lcj rk gjnb arbkq ykhanbd nkpyk! :)."
cle = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
message_dechiffre = dechiffrer_vigenere(message_chiffre, cle)
print("Message déchiffré:\n\n", message_dechiffre)
```

> En executant ce script on obtient le flag.

# Flag
```CTF_decode_the_cipher_riddle_xmfkupz```
