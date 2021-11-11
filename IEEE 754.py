
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

def base10_to_2_decimal(x):
  a=""
  if 0<=x<1:
    while x!=0:
      x=x * 2
      x=str(x)
      a=a+x[0:1]
      y=int(x[0:1])
      x=float(x)
      x=x-y
      if len(a)>23:
        break
      while len(a[0:1]) == 0:
        continue
  return a

def calibre_droite(x):
  x="0"
  while len(x)<23:
    x=x+x
  return x
