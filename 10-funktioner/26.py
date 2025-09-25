# Skapa ett textanalysverktyg med flera funktioner:
# - `räkna_tecken(text)` - räknar totala antalet tecken
# - `räkna_ord(text)` - räknar antalet ord  
# - `vanligaste_ord(text)` - hittar det vanligaste ordet - vi kan inte göra det här på ett effektivt sätt än men vi KAN göra det om vi är lite kluriga
# - `omvänd_text(text)` - vänder texten baklänges
# - En huvudfunktion som låter användaren välja vilken analys de vill göra

# Här är en början:

def skriv_ut_meny():
    print("Huvudmeny")
    print("1. Räkna tecken")
    print("2. Räkna ord")
    print("0. Avsluta programmet")
    print("Gör ett val: ")

def räkna_tecken(text):
    return len(text)

def räkna_ord(text):
    antal_mellanslag = text.count(" ")
    return antal_mellanslag + 1

def main():
    while True:
        text = input("Mata in en text: ")
        skriv_ut_meny()
        val = input()
        if val=="1":
            resultat = räkna_tecken(text)
            print(resultat)
        elif val=="2":
            resultat = räkna_ord(text)
            print(resultat)
        elif val=="0":
            break
        else:
            print("Felaktigt val.")

main()