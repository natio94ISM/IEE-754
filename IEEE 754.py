
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

def base2_16(chaine_nb_base_2):
  chaine = hex(int(chaine_nb_base_2,2))[2:]
  return calibre_gauche(chaine,8)
