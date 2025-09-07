# Det här programmet fungerar inte för att avgöra
# om ett tal är ett primtal eller inte.

# Men vi använder det för att demonstrera hur
# operatorn % eller modulo används. Resultatet
# av modulo är resten vid en heltalsdivision,
# dvs det som återstår när man delat upp talet
# i hela delar
# 10 % 3 -> 1 (3*3 hela, 1 i rest)
# 28 % 7 -> 0 (7*4 hela, 0 i rest)
# 13 % 5 -> 3 (5*2 hela, 3 i rest) 

tal = 99
# Om vi hittar tal som ger resten 0
# så har vi hittat en delare
# Ligger den mellan 2 och talet så är det
# en faktor och talet är inte ett primtal
for delare in range(2,tal):
    if tal % delare == 0:
        # Det här stämmer - vi har hittat en delare
        print("Inte ett primtal")
    else:
        # Det här stämmer inte!
        # INGA tal för vara delare
        print("Primtal")
