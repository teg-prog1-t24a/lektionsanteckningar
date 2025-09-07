# Vi kan skapa strängar med text inom dubbla citattecken
print("Hej!")

# Eller enkla
print('Hej!')

# Och om vi vill ha flera rader text med radbrytning
# så kan vi använda tre dubbla eller enkla citattecken på rad
print("""
Här kan jag skriva ett långt stycke
text som ser ut likadant när jag kör
""")

# Om vi inte tilldelar en sådan sträng till en variabel
# så gör inte programmet något med den - det blir ett alternativt
# sätt att skriva en kommentar som man ibland kan se i program.
'''Det här är typ en kommentar'''

# Strängar är itererbara eller indexerbara
namn = "Micke"
print(namn[1]) # skriver ut i, index börjar på 0
print(namn[0]) # skriver ut M

print()

# Vi kan iterera (loopa) igenom bokstäverna utan att
# använda index. Vi läser vad for-loopen gör ungefär så här
# "För VARJE bokstav i ordet NAMN gör följande:"
for bokstav in namn:
    print(bokstav)

# Samma sak går att göra med index men det ser lite
# klumpigare ut och det är större risk att vi gör fel
for idx in range(0, len(namn)):
    print(namn[idx])

# Vi kan jämföra strängar med == och !=
if namn=="Micke":
    print ("Yeah!")
else:
    print("booo!")

# Vi kan använda in för att se om en sträng finns
# inuti en annan
lärarlistan = "Anders, Tommy, Lasse, Emmy"
if namn in lärarlistan:
    print("Finns")
else:
    print("Finns inte")

# När vi jämför är det viktigt med stora och
# små tecken. Även mellanslag spelar roll.
print("Micke"=="Micke")
print("Micke"!="Micke")
print(not "Micke"=="Micke")
print("Micke"=="micke")
print("MickE"=="Micke")
print("Micke "=="Micke")

# Med hjälp av slices kan vi plocka ut
# delar av en sträng
siffror = "123456789"
print(siffror[3]) # 4
print(siffror[3:7]) # 4567
print(siffror[7:3:-1]) #8765
print(siffror[::2]) #13579
print(siffror[1::2]) #2468

# Vi har sett några funktioner som använder strängar
antal_tecken = len(siffror)
print(antal_tecken)

# Det finns också många inbyggda METODER, som är en typ av funktioner
# Vi kan använda dem genom att skriva sträng och sedan . (punkt) och
# därefter namnet på metoden. Det innebär att vi göra något med just
# den strängen som står före punkten.
f = "Finished of files f"
# Vi kan till exempel räkna tecken mycket enklare med en inbyggd metod
antal_f = f.count("f")
print(antal_f)

# Andra bra metoder kan ta bort mellanslag och göra alla bokstäver
# små eller stora - vilket ibland är mycket praktiskt när vill jämföra strängar
namn = "    miCKe  "
finaste_namnet = "Micke"
namn_utan_blanksteg_i_ändarna = namn.strip()
namn_med_små_bokstäver = namn.lower()
# Om en metod ger en ny sträng så kan vi använda flera metoder i rad
jämförbart_namn = namn.strip().lower()
if jämförbart_namn==finaste_namnet.lower():
    print("Fint!")
