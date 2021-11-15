from math import *
def signe(nb_decimal):
  if nb_decimal >=0:
       return "0"
  else:
      return "1"

def base10_2_entier(entier_base10):
    resultat = ""
    while entier_base10 != 0:
      r=entier_base10%2
      resultat=str(r)+resultat
      entier_base10=entier_base10//2

    return resultat

def calibre_gauche(chaine,nb_car):
    while len(chaine) != nb_car :
        chaine="0"+chaine
    return chaine

def puissance_de_deux(nb_decimal):
    if nb_decimal<0:
        nb_decimal=-nb_decimal
    if nb_decimal==0:
        return 0
    for i in range(-128,127):
        a=2**i
        if a > nb_decimal:
            return i-1
        elif a== nb_decimal:
            return i

def base2_16(chaine_nb_base_2):
    pos2=len(chaine_nb_base_2)
    pos1=pos2-4
    chaine_hexadecimale=""
    for i in range(0,(len(chaine_nb_base_2)//2)-1):
        partie_de_chaine=chaine_nb_base_2[pos1:pos2]
        pos1-=4
        pos2-=4
        nb_hexa=0
        if pos1<0:
          pos1=0
        if pos2<0:
            break
        for x in range (0,len(partie_de_chaine)):
          n=len(partie_de_chaine)-(x+1)
          a=int(partie_de_chaine[x])
          a=a*2**n
          nb_hexa+=a
        chaine_hexadecimale=str(nb_hexa)+chaine_hexadecimale
    for i in range(0,len(chaine_hexadecimale)):
      chaine_hexadecimale=chaine_hexadecimale.replace("10","A")
      chaine_hexadecimale=chaine_hexadecimale.replace("11","B")
      chaine_hexadecimale=chaine_hexadecimale.replace("12","C")
      chaine_hexadecimale=chaine_hexadecimale.replace("13","D")
      chaine_hexadecimale=chaine_hexadecimale.replace("14","E")
      chaine_hexadecimale=chaine_hexadecimale.replace("15","F")
      "".join(chaine_hexadecimale)
    return chaine_hexadecimale

def base10_to_2_decimal(Float,nb_chiffres_ap_virg):
  partie_entiere=floor(Float)
  partie_entiere_base2=base10_2_entier(partie_entiere)
  partie_decimale=Float-partie_entiere
  nbdecimal_base2=""
  while True:
      partie_decimale=partie_decimale*2
      partie_entiere=floor(partie_decimale)
      nbdecimal_base2+=str(partie_entiere)
      partie_decimale-=partie_entiere
      if  partie_decimale==0 or len(nbdecimal_base2)>=nb_chiffres_ap_virg:
          break
  nbdecimal_base2=partie_entiere_base2+nbdecimal_base2
  nbdecimal_base2=nbdecimal_base2[1:len(nbdecimal_base2)]
  return nbdecimal_base2

def calibre_droite(chaine,nb_car):
  while len(chaine)<nb_car:
    chaine=chaine+"0"
  return chaine

def calibre_gauche(chaine,nb_car):
  while len(chaine)<nb_car:
    chaine="0"+chaine
  return chaine

def translate_127(nb,sens):
    if sens == "+":
        assert nb <=128 and nb >=-127
        return base10_2_entier(nb+127)
    elif sens == "-":
        assert nb <=255 and nb >=0
        return base10_2_entier(nb-127)
    else:
        raise AssertionError
def presentation_result_base2(chaine_nb_base_2):
    return chaine_nb_base_2[0]+" "+chaine_nb_base_2[1:9]+" "+chaine_nb_base_2[10:33]

def IEE754(nb):
  if nb==0:
      print("bit : 0 00000000 00000000000000000000000")
      print("hexadecimal : 00000000")
  else:
      signenb=signe(nb)
      if signenb=="1":
          nb=-nb
      exposant=puissance_de_deux(nb)
      exposant_base2=translate_127(exposant,"+")
      if type(nb) is float:
          nb_base2=base10_to_2_decimal(nb,3)
          exposant_base2=calibre_gauche(exposant_base2,8)
          nb_final=str(signenb)+str(exposant_base2)+str(calibre_droite(nb_base2,23))
      else:
          print()
          nb_base2=base10_2_entier(nb)
          exposant_base2=calibre_gauche(exposant_base2,8)
          nb_final=str(signenb)+str(exposant_base2)+str(calibre_droite(nb_base2[1:len(nb_base2)],23))
      print("bit : "+presentation_result_base2(nb_final))
      print("hexadecimal : "+calibre_droite(base2_16(nb_final),8))

def fonction_depart():
    try:
        print("Quel nombre_voulez vous convertir ?")
        nb=float(input())
        IEE754(nb)
        print("Voulez-vous recommencer ?")
        rep=input()
        if rep=="oui" or rep=="Oui":
            fonction_depart()
        else:
            print("Au revoir")
    except:
        print("Veuillez recommencer !")
        fonction_depart()
fonction_depart()
