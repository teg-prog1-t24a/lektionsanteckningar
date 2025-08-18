# Använd input() för att be användaren om information
birth_year = input("När föddes du? ")
age = input("Hur gammal är du? ")

# Inmatningarna lagras som text, men i det här
# programmet vill vi räkna med dom som tal
# int() omvandlar till heltal
birth_year = int(birth_year)
age = int(age)

# Nu kan vi använda variablerna till att räkna med
current_year = birth_year + age

# För att kunna lägga ihop svaret med annan text
# kan vi omvandla tillbaka till en sträng med 
# hjälp av funktionen str()
# Det går bra att använda funktioner inuti andra funktionen
# vi måste inte lagra vårt delresultat i en variabel
print("I år är det år " + str(current_year))



