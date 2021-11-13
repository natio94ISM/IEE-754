
def signe(nb_decimal):
  if nb_decimal >=0: return "0"
  else: return "1"
  
def base10_2_entier(entier_base10):
  if entier_base10 == 0:
    resultat = "0"
  else:
    resultat = ""
    while entier_base10 != 0:
      resultat = "01" [entier_base10 % 2] + resultat
      entier_base10 = entier_base10//2
  return resultat
def calibre_gauche(chaine,nb_car):
    while len(chaine) != nb_car :
        chaine="0"+chaine
    return chaine
def puissance_de_deux(nb_decimal):
    for i in range(-128,127):
        a=2**i
        if a >= nb_decimal:
            n=i
            break
    return n

def base2_16(chaine_nb_base_2):
  chaine = hex(int(chaine_nb_base_2,2))[2:]
  return calibre_gauche(chaine,8)

def base10_to_2_decimal(Float,nb_chiffres_ap_virg):
  nb_chiffres_ap_virg=""
  if 0<=Float<1:
    while xFloat!=0:
      Float=Float * 2
      Float=str(Float)
      nb_chiffres_ap_virg=nb_chiffres_ap_virg+Float[0:1]
      y=int(Float[0:1])
      Float=float(Float)
      Float=Float-y
      if len(nb_chiffres_ap_virg)>23:
        break
      while len(anb_chiffres_ap_virg[0:1]) == 0:
        continue
  return nb_chiffres_ap_virg

def calibre_droite(chaine,nb_car):
  while len(chaine)<23:
    nb_car=chaine+"0"  
  return nb_car

def calibre_gauche(chaine,nb_car):
  while len(chaine)<23:
    nb_car="0"chaine
  return nb_car  
