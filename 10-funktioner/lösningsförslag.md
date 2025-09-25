# Lösningsförslag - Funktioner

## E-uppgifter

### Uppgift 1 – Enkel funktion

```python
def hälsa():
    print("Hej världen!")

hälsa()
```

---

### Uppgift 2 – Funktion med parameter

```python
def hälsa_person(namn):
    print(f"Hej {namn}!")

hälsa_person("Micke")
```

---

### Uppgift 3 – Enkel returvärde

```python
def dubbla(tal):
    return tal * 2

print(dubbla(4))
print(dubbla(16))
print(dubbla(100))
```

---

### Uppgift 4 – Addition

```python
def addera(tal1, tal2):
    return tal1 + tal2

print(addera(14, 27))
```

---

### Uppgift 5 – Kvadrat

```python
def kvadrat(tal):
    return tal ** 2

print(kvadrat(12))
print(kvadrat(-5))
```

---

### Uppgift 6 – Slumpmässigt tal

```python
import random

def slumptal():
    return random.randint(1, 10)

print(slumptal())
print(slumptal())
print(slumptal())
print(slumptal())
```

---

### Uppgift 7 – Versaler funktion

```python
def skriv_högt(text):
    print(f"{text.upper()}!")

skriv_högt("hej alla")
```

---

### Uppgift 8 – Är jämnt

```python
def är_jämnt(tal):
    return tal % 2 == 0

# Alternativt med if-sats (längre variant)
def är_jämnt2(tal):
    if tal % 2 == 0:
        return True
    else:
        return False

print(är_jämnt(4))  # True
print(är_jämnt(5))  # False
```

---

### Uppgift 9 – Största talet

```python
def största(tal1, tal2):
    if tal1 > tal2:
        return tal1
    else:
        return tal2

# Alternativt kortare med max()
def största2(tal1, tal2):
    return max(tal1, tal2)

print(största(10, 15))
```

---

### Uppgift 10 – Personlig presentation

```python
def presentera(namn, ålder):
    print(f"Jag heter {namn} och är {ålder} år gammal.")

presentera("Micke", 50)
```

---

### Uppgift 11 – Cirkelns area

```python
import math

def cirkel_area(radie):
    return math.pi * radie * radie

# Alternativt med radie**2
def cirkel_area2(radie):
    return math.pi * radie**2

print(cirkel_area(5))
```

---

### Uppgift 12 – Temperaturomvandling

```python
def celsius_till_fahrenheit(celsius):
    return celsius * 9/5 + 32

print(celsius_till_fahrenheit(37))  # Kroppstemperatur
print(celsius_till_fahrenheit(0))   # Fryspunkt
print(celsius_till_fahrenheit(100)) # Kokpunkt
```

---

## C-uppgifter

### Uppgift 13 – Kasta tärning flera gånger

```python
import random

def kasta_tärningar(antal):
    tärningar = []
    for _ in range(antal):
        tärning = random.randint(1, 6)
        tärningar.append(tärning)
    return tärningar

# Alternativt med list comprehension
def kasta_tärningar2(antal):
    return [random.randint(1, 6) for _ in range(antal)]

print(kasta_tärningar(3))
print(kasta_tärningar(5))
```

---

### Uppgift 14 – Medelvärdeskalkylator

```python
def medelvärde(lista):
    return sum(lista) / len(lista)

# Alternativt från grunden
def medelvärde2(lista):
    summa = 0
    antal = 0
    for tal in lista:
        summa += tal
        antal += 1
    return summa / antal

print(medelvärde([1, 2, 3, 4, 5]))
```

---

### Uppgift 15 – Faktorial

```python
def faktorial(n):
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
    return resultat

# Alternativt med rekursion (avancerat)
def faktorial2(n):
    if n <= 1:
        return 1
    else:
        return n * faktorial2(n - 1)

print(faktorial(5))  # 120
```

---

### Uppgift 16 – Kontrollera primtal

```python
def är_primtal(tal):
    if tal < 2:
        return False
    for x in range(2, int(tal**0.5) + 1):
        if tal % x == 0:
            return False
    return True

print(är_primtal(17))  # True
print(är_primtal(18))  # False
```

---

### Uppgift 17 – Stränganalys

```python
def analysera_sträng(text):
    antal_tecken = len(text)
    antal_ord = len(text.split())
    antal_vokaler = 0
    vokaler = "aeiuoyåäö"
    
    for tecken in text.lower():
        if tecken in vokaler:
            antal_vokaler += 1
    
    return (antal_tecken, antal_ord, antal_vokaler)

print(analysera_sträng("Hej på dig"))
```

---

### Uppgift 18 – Lista med villkor

```python
def filtrera_jämna(lista):
    jämna = []
    for tal in lista:
        if tal % 2 == 0:
            jämna.append(tal)
    return jämna

# Alternativt med list comprehension
def filtrera_jämna2(lista):
    return [x for x in lista if x % 2 == 0]

print(filtrera_jämna([1, 2, 3, 4, 5, 6]))
```

---

### Uppgift 19 – Lösenordsgenerator

```python
import random

def generera_lösenord(längd):
    bokstäver = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    siffror = "0123456789"
    tecken = bokstäver + siffror
    
    lösenord = ""
    for _ in range(längd):
        index = random.randint(0, len(tecken) - 1)
        lösenord += tecken[index]
    return lösenord

# Alternativt med string-modulen (lite mer avancerat)
# och en annan random-funktion (googla för detaljer)
import string
def generera_lösenord2(längd):
    tecken = string.ascii_letters + string.digits
    lösenord = ""
    for _ in range(längd):
        lösenord += random.choice(tecken)
    return lösenord

print(generera_lösenord(8))
```

---

### Uppgift 20 – Betygskonvertering

```python
def poäng_till_betyg(poäng):
    if poäng >= 90:
        return "A"
    elif poäng >= 80:
        return "B"
    elif poäng >= 70:
        return "C"
    elif poäng >= 60:
        return "D"
    elif poäng >= 50:
        return "E"
    else:
        return "F"

print(poäng_till_betyg(85))  # B
print(poäng_till_betyg(45))  # F
```

---

### Uppgift 21 – Räkna ord

```python
def räkna_ord(text, sökord):
    ord_lista = text.lower().split()
    return ord_lista.count(sökord.lower())

print(räkna_ord("Hej hej alla hej", "hej"))
```

---

### Uppgift 22 – Geometriska former

```python
def rektangel_area(längd, bredd):
    return längd * bredd

def rektangel_omkrets(längd, bredd):
    return 2 * (längd + bredd)

def triangel_area(bas, höjd):
    return 0.5 * bas * höjd

print(rektangel_area(5, 3))
print(rektangel_omkrets(5, 3))
print(triangel_area(4, 6))
```

---

### Uppgift 23 – Validering av input

```python
def validera_ålder(ålder_str):
    if ålder_str.isnumeric():
        ålder = int(ålder_str)
        return 0 <= ålder <= 120
    else:
        return False

print(validera_ålder("25"))   # True
print(validera_ålder("abc"))  # False
print(validera_ålder("150"))  # False
```

---

### Uppgift 24 – Fibonacci-tal

```python
def fibonacci(n):
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Alternativt med rekursion (långsamt för stora n)
def fibonacci2(n):
    if n <= 1:
        return n
    return fibonacci2(n - 1) + fibonacci2(n - 2)

print(fibonacci(10))  # 55
```

---

## A-uppgifter

### Uppgift 25 – Enkel kalkylator

```python
def addera(a, b):
    return a + b

def subtrahera(a, b):
    return a - b

def multiplicera(a, b):
    return a * b

def dividera(a, b):
    if b == 0:
        return "Fel: Division med noll!"
    return a / b

def kalkylator():
    while True:
        print("\nKalkylator")
        print("1. Addition")
        print("2. Subtraktion") 
        print("3. Multiplikation")
        print("4. Division")
        print("0. Avsluta")
        
        val = input("Välj operation: ")
        
        if val == "0":
            break
        elif val in ["1", "2", "3", "4"]:
            a = float(input("Första talet: "))
            b = float(input("Andra talet: "))
            
            if val == "1":
                print(f"Resultat: {addera(a, b)}")
            elif val == "2":
                print(f"Resultat: {subtrahera(a, b)}")
            elif val == "3":
                print(f"Resultat: {multiplicera(a, b)}")
            elif val == "4":
                print(f"Resultat: {dividera(a, b)}")
        else:
            print("Ogiltigt val!")

# kalkylator()  # Avkommentera för att testa
```

---

### Uppgift 26 – Textanalysverktyg

```python
def räkna_tecken(text):
    return len(text)

def räkna_ord(text):
    return len(text.split())

def vanligaste_ord(text):
    ord_lista = text.lower().split()
    if not ord_lista:
        return None
    
    # Räkna förekomster
    ord_antal = {}
    for ord in ord_lista:
        ord_antal[ord] = ord_antal.get(ord, 0) + 1
    
    # Hitta vanligaste
    vanligast = max(ord_antal, key=ord_antal.get)
    return vanligast, ord_antal[vanligast]

def omvänd_text(text):
    return text[::-1]

def textanalys():
    while True:
        text = input("\nMata in text att analysera: ")
        
        print("\nVälj analys:")
        print("1. Räkna tecken")
        print("2. Räkna ord")
        print("3. Vanligaste ord")
        print("4. Omvänd text")
        print("0. Avsluta")
        
        val = input("Ditt val: ")
        
        if val == "0":
            break
        elif val == "1":
            print(f"Antal tecken: {räkna_tecken(text)}")
        elif val == "2":
            print(f"Antal ord: {räkna_ord(text)}")
        elif val == "3":
            resultat = vanligaste_ord(text)
            if resultat:
                ord, antal = resultat
                print(f"Vanligaste ord: '{ord}' ({antal} gånger)")
            else:
                print("Ingen text att analysera")
        elif val == "4":
            print(f"Omvänd text: {omvänd_text(text)}")
        else:
            print("Ogiltigt val!")

# textanalys()  # Avkommentera för att testa
```

---

### Uppgift 27 – Bankonto-simulator

```python
def skapa_konto(startbelopp):
    return startbelopp

def sätt_in(balans, belopp):
    if belopp > 0:
        return balans + belopp
    else:
        print("Belopp måste vara positivt!")
        return balans

def ta_ut(balans, belopp):
    if belopp > 0:
        if belopp <= balans:
            return balans - belopp
        else:
            print("Otillräckligt saldo!")
            return balans
    else:
        print("Belopp måste vara positivt!")
        return balans

def visa_balans(balans):
    print(f"Nuvarande saldo: {balans:.2f} kr")

def ränta(balans, räntesats):
    return balans * (1 + räntesats / 100)

def banksimulator():
    balans = float(input("Ange startbelopp: "))
    
    while True:
        print("\nBankonto - Huvudmeny")
        print("1. Visa saldo")
        print("2. Sätt in pengar")
        print("3. Ta ut pengar")
        print("4. Beräkna ränta")
        print("0. Avsluta")
        
        val = input("Ditt val: ")
        
        if val == "0":
            break
        elif val == "1":
            visa_balans(balans)
        elif val == "2":
            belopp = float(input("Belopp att sätta in: "))
            balans = sätt_in(balans, belopp)
        elif val == "3":
            belopp = float(input("Belopp att ta ut: "))
            balans = ta_ut(balans, belopp)
        elif val == "4":
            räntesats = float(input("Ränta i procent: "))
            ny_balans = ränta(balans, räntesats)
            print(f"Saldo efter ränta: {ny_balans:.2f} kr")
            balans = ny_balans
        else:
            print("Ogiltigt val!")

# banksimulator()  # Avkommentera för att testa
```

---

### Uppgift 28 – Spel: Gissa numret (avancerat)

```python
import random

def välj_svårighetsgrad():
    print("Välj svårighetsgrad:")
    print("1. Lätt (1-10)")
    print("2. Medium (1-50)")
    print("3. Svår (1-100)")
    
    while True:
        val = input("Ditt val: ")
        if val == "1":
            return 1, 10
        elif val == "2":
            return 1, 50
        elif val == "3":
            return 1, 100
        else:
            print("Ogiltigt val!")

def generera_hemligt_tal(min_val, max_val):
    return random.randint(min_val, max_val)

def få_gissning():
    while True:
        inp = input("Din gissning: ")
        if inp.isnumeric():
            return int(inp)

def ge_tips(gissning, hemligt_tal):
    # abs returnerar absolutbelopper av sitt argument
    skillnad = abs(gissning - hemligt_tal)
    if gissning < hemligt_tal:
        if skillnad > 10:
            print("Mycket för lågt!")
        elif skillnad > 5:
            print("För lågt!")
        else:
            print("Lite för lågt!")
    else:
        if skillnad > 10:
            print("Mycket för högt!")
        elif skillnad > 5:
            print("För högt!")
        else:
            print("Lite för högt!")

def spela_spel():
    min_val, max_val = välj_svårighetsgrad()
    hemligt_tal = generera_hemligt_tal(min_val, max_val)
    antal_gissningar = 0
    max_gissningar = 7
    
    print(f"\nJag tänker på ett tal mellan {min_val} och {max_val}")
    print(f"Du har {max_gissningar} gissningar på dig!")
    
    while antal_gissningar < max_gissningar:
        gissning = få_gissning()
        antal_gissningar += 1
        
        if gissning == hemligt_tal:
            print(f"Grattis! Du gissade rätt på {antal_gissningar} försök!")
            if antal_gissningar == 1:
                print("Fantastiskt! Du gissade rätt på första försöket!")
            elif antal_gissningar <= 3:
                print("Mycket bra!")
            elif antal_gissningar <= 5:
                print("Bra jobbat!")
            return
        else:
            ge_tips(gissning, hemligt_tal)
            kvar = max_gissningar - antal_gissningar
            if kvar > 0:
                print(f"Du har {kvar} gissningar kvar.")
    
    print(f"Tyvärr, du klarade det inte. Talet var {hemligt_tal}.")

# spela_spel()  # Avkommentera för att testa
```

---

### Uppgift 29 – Elevregister

```python
def lägg_till_elev(register, namn):
    # Kontrollera om eleven redan finns
    for elev in register:
        if elev[0] == namn:
            print(f"Eleven {namn} finns redan!")
            return register
    register.append([namn, []])  # [namn, [betyg]]
    print(f"Eleven {namn} tillagd!")
    return register

def lägg_till_betyg(register, namn, ämne, betyg):
    for elev in register:
        if elev[0] == namn:
            elev[1].append((ämne, betyg))
            print(f"Betyg {betyg} i {ämne} tillagt för {namn}")
            return register
    print(f"Eleven {namn} finns inte!")
    return register

def betyg_till_poäng(betyg):
    if betyg == "A":
        return 20
    elif betyg == "B":
        return 17.5
    elif betyg == "C":
        return 15
    elif betyg == "D":
        return 12.5
    elif betyg == "E":
        return 10
    elif betyg == "F":
        return 0
    else:
        return 0

def beräkna_medelbetyg(register, namn):
    for elev in register:
        if elev[0] == namn:
            if not elev[1]:
                return 0
            summa = 0
            for ämne, betyg in elev[1]:
                summa += betyg_till_poäng(betyg)
            return summa / len(elev[1])
    return None

def hitta_bästa_elev(register):
    if not register:
        return None
    
    bästa_elev = None
    högsta_medel = -1
    
    for elev in register:
        medel = beräkna_medelbetyg(register, elev[0])
        if medel and medel > högsta_medel:
            högsta_medel = medel
            bästa_elev = elev[0]
    
    return bästa_elev, högsta_medel

def visa_alla_elever(register):
    if not register:
        print("Inga elever registrerade.")
        return
    
    for elev in register:
        namn = elev[0]
        betyg = elev[1]
        print(f"\n{namn}:")
        if betyg:
            for ämne, betyg_värde in betyg:
                print(f"  {ämne}: {betyg_värde}")
            medel = beräkna_medelbetyg(register, namn)
            print(f"  Medelbetyg: {medel:.2f}")
        else:
            print("  Inga betyg registrerade")

def elevregister():
    register = []
    
    while True:
        print("\nElevregister")
        print("1. Lägg till elev")
        print("2. Lägg till betyg")
        print("3. Visa alla elever")
        print("4. Hitta bästa elev")
        print("0. Avsluta")
        
        val = input("Ditt val: ")
        
        if val == "0":
            break
        elif val == "1":
            namn = input("Elevens namn: ")
            register = lägg_till_elev(register, namn)
        elif val == "2":
            namn = input("Elevens namn: ")
            ämne = input("Ämne: ")
            betyg = input("Betyg (A-F): ").upper()
            if betyg in ["A", "B", "C", "D", "E", "F"]:
                register = lägg_till_betyg(register, namn, ämne, betyg)
            else:
                print("Ogiltigt betyg!")
        elif val == "3":
            visa_alla_elever(register)
        elif val == "4":
            resultat = hitta_bästa_elev(register)
            if resultat:
                namn, medel = resultat
                print(f"Bästa elev: {namn} (medelbetyg: {medel:.2f})")
            else:
                print("Inga elever med betyg.")
        else:
            print("Ogiltigt val!")

# elevregister()  # Avkommentera för att testa
```

---

### Uppgift 30 – Enkel kryptografi

```python
def kryptera_bokstav(bokstav, förskjutning):
    if bokstav.isalpha():
        # Hantera svenska bokstäver enkelt genom att bara använda a-z
        # ord returnerar ett ordningstal för ett tecken
        # char returnerar tecknet för ett tal
        # men det fungerar bara för amerikanska bokstäver och tecken
        if bokstav.islower():
            return chr((ord(bokstav) - ord('a') + förskjutning) % 26 + ord('a'))
        else:
            return chr((ord(bokstav) - ord('A') + förskjutning) % 26 + ord('A'))
    return bokstav

def kryptera_text(text, förskjutning):
    krypterad = ""
    for bokstav in text:
        krypterad += kryptera_bokstav(bokstav, förskjutning)
    return krypterad

def dekryptera_text(krypterad_text, förskjutning):
    return kryptera_text(krypterad_text, -förskjutning)

def knäck_kod(krypterad_text):
    print("Försöker knäcka koden genom att testa alla förskjutningar:")
    for förskjutning in range(26):
        dekrypterad = dekryptera_text(krypterad_text, förskjutning)
        print(f"Förskjutning {förskjutning}: {dekrypterad}")

def kryptografi():
    while True:
        print("\nCaesar-kryptering")
        print("1. Kryptera text")
        print("2. Dekryptera text")
        print("3. Knäck kod")
        print("0. Avsluta")
        
        val = input("Ditt val: ")
        
        if val == "0":
            break
        elif val == "1":
            text = input("Text att kryptera: ")
            # Try går att använda för att fånga fel
            # Det går att skriva koden med .isnumeric()
            # men på den här nivån är det värt att googla
            # för att lära sig något nytt
            try:
                förskjutning = int(input("Förskjutning (1-25): "))
                if 1 <= förskjutning <= 25:
                    krypterad = kryptera_text(text, förskjutning)
                    print(f"Krypterad text: {krypterad}")
                else:
                    print("Förskjutning måste vara mellan 1-25!")
            except ValueError:
                print("Ogiltig förskjutning!")
        elif val == "2":
            text = input("Text att dekryptera: ")
            # Se kommentar om try ovan
            try:
                förskjutning = int(input("Förskjutning: "))
                dekrypterad = dekryptera_text(text, förskjutning)
                print(f"Dekrypterad text: {dekrypterad}")
            except ValueError:
                print("Ogiltig förskjutning!")
        elif val == "3":
            text = input("Text att knäcka: ")
            knäck_kod(text)
        else:
            print("Ogiltigt val!")

# kryptografi()  # Avkommentera för att testa
```

---

## Tips för lösningsförslag

### Vanliga misstag att undvika:
- Glöm inte `return` i funktioner som ska returnera värden
- Kontrollera att parametrar har rätt datatyp
- Hantera felfall (division med noll, tomma listor, etc.)
- Testa funktioner med olika värden, inklusive kantfall

### Kodkvalitet:
- Använd beskrivande funktionsnamn
- Skriv korta funktioner som gör en sak
- Kommentera komplicerad kod
- Validera input när det behövs

### Testning:
```python
# Exempel på hur man testar funktioner
print(f"kvadrat(5) = {kvadrat(5)}")        # Förväntat: 25
print(f"är_jämnt(4) = {är_jämnt(4)}")      # Förväntat: True
print(f"är_jämnt(5) = {är_jämnt(5)}")      # Förväntat: False
```
