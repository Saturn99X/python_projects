print(" £££££££££££  BIENVENUE DANS CE PROGRAMME DE CONVERSION  ££££££££ ")
print()
print("voulez vous convertir de pouces vers centimetre ou de centimetre vers pouces . (A = centimetre ==> POUCES B = POUCES ==> centimetre)")
Choix = input(" quelle est votre choix   ? ")
nombre = float(input("entrer le nombre a convertir :  "))
while nombre == " " :
    nombre = float(input("entrer le nombre a convertir :  "))
if Choix == "a" or "A" :
    resultat_conversion_centimetre = nombre / 2.54 
    print("la conversion de " , nombre , "cm = " , resultat_conversion_centimetre , "POUCES" )
elif Choix == "b" or"B" :
    resultat_conversion_POUCES = nombre * 2.54 
    print("la conversion de " , nombre , "pouces  = " , resultat_conversion_POUCES , "cm" )

