def signe(nb_decimal):
    if nb_decimal<0:
        return "1"
    elif nb_decimal>0:
        return "0"
def puissance_de_deux(nb_decimal):
    for i in range(-128,127):
        a=2**i
        if a >= nb_decimal:
            n=i
            break
    return n
def base10_to_2_entier(entier_base10):
    nb_base2=""
    a=entier_base10
    while a>=1:
        r=a%2
        nb_base2=str(r)+nb_base2
        a=a//2
    return nb_base2
def calibre_gauche(chaine,nb_car):
    while len(chaine) != nb_car :
        chaine="0"+chaine
    return chaine
def calibre_droite(chaine,nb_car):
    while len(chaine)!=nb_car:
        chaine=chaine+"0"
    return chaine
def base10_to_2_decimal(partie_decimale,nb_chiffres_ap_virg):
    assert partie_decimale >= 1 or partie_decimale <0
