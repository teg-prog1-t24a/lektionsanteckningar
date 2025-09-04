print("Hej!")
print('Hej!')
print("""
Här kan jag skriva ett långt stycke
text som ser ut likadant när jag kör
""")

# Det här är en kommentar
'''Det här är typ en kommentar'''

# Strängar är itererbara eller indexerbara
namn = "Micke"
print(namn[1]) # skriver ut i, index börjar på 0
print(namn[0]) # skriver ut M

print()

for bokstav in namn:
    print(bokstav)

for idx in range(0, len(namn)):
    print(namn[idx])

if namn=="Micke":
    print ("Yeah!")
else:
    print("booo!")

lärarlistan = "Anders, Tommy, Lasse, Emmy"
if namn in lärarlistan:
    print("Finns")
else:
    print("Finns inte")

print("Micke"=="Micke")
print("Micke"!="Micke")
print(not "Micke"=="Micke")
print("Micke"=="micke")
print("MickE"=="Micke")
print("Micke "=="Micke")

# slices
siffror = "123456789"
print(siffror[3]) # 4
print(siffror[3:7]) # 4567
print(siffror[7:3:-1]) #8765
print(siffror[::2]) #13579
print(siffror[1::2]) #2468

# Funktioner på strängar
antal_tecken = len(siffror)
print(antal_tecken)

# Metoder på strängar
f = "Finished of files f"
antal_f = f.count("f")
print(antal_f)

namn = "    miCKe...,  "
finaste_namnet = "Micke"
namn_utan_blanksteg_i_ändarna = namn.strip()
namn_med_små_bokstäver = namn.lower()
jämförbart_namn = namn.strip().lower()
if jämförbart_namn==finaste_namnet.lower():
    print("Fint!")

antal_i = namn.count("i")
