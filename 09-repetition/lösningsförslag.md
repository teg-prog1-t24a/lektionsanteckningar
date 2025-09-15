# Lösningsförslag - Blandade övningsuppgifter

## E-uppgifter

### Uppgift 1 – Grundläggande variabler

```python
namn = "Micke"
ålder = 50
print(f"Jag heter {namn} och är {ålder} år gammal")
```

---

### Uppgift 2 – Enkel aritmetik

```python
tal1 = float(input("Ange första talet: "))
tal2 = float(input("Ange andra talet: "))

summa = tal1 + tal2
skillnad = tal1 - tal2
produkt = tal1 * tal2

print(f"Summa: {summa}")
print(f"Skillnad: {skillnad}")
print(f"Produkt: {produkt}")
```

---

### Uppgift 3 – Jämförelse

```python
tal1 = 15
tal2 = 10

if tal1 > tal2:
    print(f"{tal1} är större än {tal2}")
elif tal1 < tal2:
    print(f"{tal1} är mindre än {tal2}")
else:
    print(f"{tal1} är lika med {tal2}")
```

---

### Uppgift 4 – Enkelt villkor

```python
ålder = int(input("Hur gammal är du? "))

if ålder >= 18:
    print("Du får rösta")
else:
    print("Du får inte rösta än")
```

---

### Uppgift 5 – Strängindexering

```python
namn = "Michael"
print(f"Första bokstaven: {namn[0]}")
print(f"Sista bokstaven: {namn[-1]}")
```

---

### Uppgift 6 – Lista med tal

```python
tal = [3, 7, 12, 5, 9]
print(f"Lista: {tal}")
print(f"Längd: {len(tal)}")
```

---

### Uppgift 7 – Tuple med koordinater

```python
koordinater = (5, 3)
print(f"x: {koordinater[0]}, y: {koordinater[1]}")
```

---

### Uppgift 8 – Enkel loop

```python
for i in range(1, 6):
    print(i)
```

---

### Uppgift 9 – Typkonvertering

```python
tal_sträng = input("Ange ett tal: ")
tal = int(tal_sträng)
resultat = tal * 2
print(f"Talet multiplicerat med 2: {resultat}")
```

---

### Uppgift 10 – Strängmetod

```python
text = "HeLLo WoRLd"
print(f"Versaler: {text.upper()}")
print(f"Gemener: {text.lower()}")
```

---

### Uppgift 11 – While-loop

```python
tal = 2
while tal <= 10:
    print(tal)
    tal += 2
```

---

### Uppgift 12 – Lista med strängar

```python
städer = ["Stockholm", "Göteborg", "Malmö"]
for stad in städer:
    print(stad)
```

---

## C-uppgifter

### Uppgift 13 – Gissa talet

```python
import random

datorns_tal = random.randint(1, 10)
gissning = int(input("Gissa ett tal mellan 1 och 10: "))

if gissning == datorns_tal:
    print("Rätt! Du gissade rätt!")
else:
    print(f"Fel! Rätt svar var {datorns_tal}")
```

---

### Uppgift 14 – Faktorisering

```python
tal = int(input("Ange ett heltal: "))
print(f"Faktorer av {tal}:")

for i in range(1, tal + 1):
    if tal % i == 0:
        print(i)
```

---

### Uppgift 15 – Medelvärde från input

```python
tal1 = float(input("Ange första talet: "))
tal2 = float(input("Ange andra talet: "))
tal3 = float(input("Ange tredje talet: "))

medelvärde = (tal1 + tal2 + tal3) / 3
print(f"Medelvärdet är: {medelvärde:.2f}")
```

---

### Uppgift 16 – Sträng-analys

```python
ord = input("Ange ett ord: ")
vokaler = "aeiouyåäö"
antal_vokaler = 0

for bokstav in ord.lower():
    if bokstav in vokaler:
        antal_vokaler += 1

print(f"Ordets längd: {len(ord)}")
print(f"Ordet baklänges: {ord[::-1]}")
print(f"Antal vokaler: {antal_vokaler}")
```

---

### Uppgift 17 – List-manipulation

```python
tal_lista = []

for i in range(5):
    tal = float(input(f"Ange tal {i+1}: "))
    tal_lista.append(tal)

print(f"Hela listan: {tal_lista}")
print(f"Största talet: {max(tal_lista)}")
print(f"Minsta talet: {min(tal_lista)}")
print(f"Summan: {sum(tal_lista)}")
```

---

### Uppgift 18 – Multiplikationstabell

```python
tal = int(input("Ange ett tal: "))

print(f"Multiplikationstabell för {tal}:")
for i in range(1, 11):
    print(f"{tal} * {i} = {tal * i}")
```

---

### Uppgift 19 – Tuple unpacking

```python
personer = [("Micke", 50), ("Agneta", 76), ("Kjell-Åke", 77)]

for namn, ålder in personer:
    print(f"{namn} är {ålder} år gammal")
```

---

### Uppgift 20 – Villkor med logiska operatorer

```python
tal = int(input("Ange ett tal: "))

if tal > 0 and tal % 2 == 0:
    print(f"{tal} är positivt och jämnt")
if tal < 0 or tal > 100:
    print(f"{tal} är negativt och/eller större än 100")
if tal != 0:
    print(f"{tal} är INTE lika med 0")
```

---

### Uppgift 21 – Slicing och bearbetning

```python
text = "Programmering är kul!"

första_tre = text[:3]
sista_tre = text[-3:]
vartannat = text[::2]

print(f"Första tre tecken: {första_tre}")
print(f"Sista tre tecken: {sista_tre}")
print(f"Vartannat tecken: {vartannat}")
```

---

### Uppgift 22 – Nästlade villkor (Skottår)

```python
år = int(input("Ange ett årtal: "))

ix
if år % 4 == 0:
    if år % 100 == 0:
        if år % 400 == 0:
            print(f"{år} är ett skottår")
        else:
            print(f"{år} är inte ett skottår")
    else:
        print(f"{år} är ett skottår")
else:
    print(f"{år} är inte ett skottår")
```

---

### Uppgift 23 – Lista med villkor

```python
import random

tal_lista = []
for i in range(10):
    tal_lista.append(random.randint(1, 20))

större_än_10 = 0
jämna_tal = 0

for tal in tal_lista:
    if tal > 10:
        större_än_10 += 1
    if tal % 2 == 0:
        jämna_tal += 1

print(f"Lista: {tal_lista}")
print(f"Antal tal större än 10: {större_än_10}")
print(f"Antal jämna tal: {jämna_tal}")
```

---

### Uppgift 24 – Break i loop

```python
summa = 0

while True:
    inmatning = input("Ange ett tal (eller 'stopp' för att avsluta): ")
    
    if inmatning.lower() == "stopp":
        break
    
    tal = float(inmatning)
    summa += tal

print(f"Summan av alla tal: {summa}")
```

---

## A-uppgifter

### Uppgift 25 – Lösenordsvalidering

```python
lösenord = input("Ange ett lösenord: ")

längd_ok = len(lösenord) >= 8
har_siffra = False
har_stor_bokstav = False
har_liten_bokstav = False

for tecken in lösenord:
    if tecken.isdigit():
        har_siffra = True
    elif tecken.isupper():
        har_stor_bokstav = True
    elif tecken.islower():
        har_liten_bokstav = True

if längd_ok and har_siffra and har_stor_bokstav and har_liten_bokstav:
    print("Lösenordet är starkt!")
else:
    print("Lösenordet är svagt. Krav som saknas:")
    if not längd_ok:
        print("- Minst 8 tecken")
    if not har_siffra:
        print("- Minst en siffra")
    if not har_stor_bokstav:
        print("- Minst en stor bokstav")
    if not har_liten_bokstav:
        print("- Minst en liten bokstav")
```

---

### Uppgift 26 – Anagram-detektor

```python
ord1 = input("Ange första ordet: ").lower()
ord2 = input("Ange andra ordet: ").lower()

# Sorterar bokstäverna i båda orden
sorterat_ord1 = sorted(ord1)
sorterat_ord2 = sorted(ord2)

if sorterat_ord1 == sorterat_ord2:
    print(f"'{ord1}' och '{ord2}' är anagram!")
else:
    print(f"'{ord1}' och '{ord2}' är inte anagram.")
```

---

### Uppgift 27 – Enkel statistik

```python
tal_lista = []

while True:
    inmatning = input("Ange ett tal (eller 'klar' för att avsluta): ")
    
    if inmatning.lower() == "klar":
        break
    
    tal = float(inmatning)
    tal_lista.append(tal)

if len(tal_lista)>0:
    antal = len(tal_lista)
    medelvärde = sum(tal_lista) / antal
    största = max(tal_lista)
    minsta = min(tal_lista)
    
    över_medel = 0
    for tal in tal_lista:
        if tal > medelvärde:
            över_medel += 1
    
    print(f"Antal tal: {antal}")
    print(f"Medelvärde: {medelvärde:.2f}")
    print(f"Största talet: {största}")
    print(f"Minsta talet: {minsta}")
    print(f"Antal tal över medelvärdet: {över_medel}")
else:
    print("Inga tal matades in.")
```

---

### Uppgift 28 – Matris-operationer

```python
import random

# Skapa 3x3 matris
matris = []
for rad in range(3):
    ny_rad = []
    for kolumn in range(3):
        ny_rad.append(random.randint(1, 9))
    matris.append(ny_rad)

# Skriv ut matrisen
print("Matris:")
for rad in matris:
    print(rad)

# Summa av varje rad
print("\nSumma av rader:")
for i, rad in enumerate(matris):
    print(f"Rad {i+1}: {sum(rad)}")

# Summa av varje kolumn
print("\nSumma av kolumner:")
for kolumn in range(3):
    kolumn_summa = 0
    for rad in range(3):
        kolumn_summa += matris[rad][kolumn]
    print(f"Kolumn {kolumn+1}: {kolumn_summa}")

# Diagonal summa
diagonal_summa = matris[0][0] + matris[1][1] + matris[2][2]
print(f"\nDiagonal summa: {diagonal_summa}")
```

---

### Uppgift 29 – Ordfrekvens

```python
mening = input("Ange en mening: ")
ord_lista = mening.lower().split()

# Räkna frekvens
hittade_ord = []
frekvens_lista = []
max_frekvens = 0
for word in ord_lista:
    if word not in hittade_ord:
        hittade_ord.append(word)
        frekvens = ord_lista.count(word)
        print(f"{word}: {frekvens}")
        frekvens_lista.append((word, frekvens))
        if frekvens > max_frekvens:
            max_frekvens = frekvens

for i in range(max_frekvens-1, -1, -1):
    for word, antal in frekvens_lista:
        if antal == i:
            print(f"{word}: {antal}")
```

---

### Uppgift 30 – Fibonacci-sekvens

```python
antal_termer = int(input("Hur många termer i Fibonacci-sekvensen? "))

fibonacci = []

if antal_termer >= 1:
    fibonacci.append(0)
if antal_termer >= 2:
    fibonacci.append(1)

for i in range(2, antal_termer):
    nästa_tal = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(nästa_tal)

print(f"Fibonacci-sekvens med {antal_termer} termer:")
print(fibonacci)
```

---

### Uppgift 31 – Primtals-detektor med lista

```python
testade_primtal = []

while True:
    tal = int(input("Ange ett tal (0 för att avsluta): "))
    
    if tal == 0:
        break
    
    if tal < 2:
        print(f"{tal} är inte ett primtal")
        continue
    
    är_primtal = True
    delare = []
    
    for i in range(2, tal):
        if tal % i == 0:
            är_primtal = False
            delare.append(i)
    
    if är_primtal:
        print(f"{tal} är ett primtal!")
        testade_primtal.append(tal)
    else:
        print(f"{tal} är inte ett primtal. Delare: {delare}")

print(f"Alla primtal som testats: {testade_primtal}")
```

---

### Uppgift 32 – Tärningsspel

```python
import random

spelare1_vinster = 0
spelare2_vinster = 0
spelare1_kast = []
spelare2_kast = []

print("Tärningsspel - 5 omgångar")
print("-------------------------")

for omgång in range(1, 6):
    kast1 = random.randint(1, 6)
    kast2 = random.randint(1, 6)
    
    spelare1_kast.append(kast1)
    spelare2_kast.append(kast2)
    
    print(f"Omgång {omgång}: Spelare 1 = {kast1}, Spelare 2 = {kast2}")
    
    if kast1 > kast2:
        print("Spelare 1 vinner!")
        spelare1_vinster += 1
    elif kast2 > kast1:
        print("Spelare 2 vinner!")
        spelare2_vinster += 1
    else:
        print("Oavgjort!")
    print()

# Visa resultat
print("SLUTRESULTAT:")
print(f"Spelare 1: {spelare1_vinster} vinster")
print(f"Spelare 2: {spelare2_vinster} vinster")

if spelare1_vinster > spelare2_vinster:
    print("Spelare 1 vinner hela spelet!")
elif spelare2_vinster > spelare1_vinster:
    print("Spelare 2 vinner hela spelet!")
else:
    print("Hela spelet slutade oavgjort!")

# Statistik
medel1 = sum(spelare1_kast) / len(spelare1_kast)
medel2 = sum(spelare2_kast) / len(spelare2_kast)

print(f"\nStatistik:")
print(f"Spelare 1 - Genomsnittskast: {medel1:.1f}")
print(f"Spelare 2 - Genomsnittskast: {medel2:.1f}")
```

---

### Uppgift 33 – Text-kryptering

```python
text = input("Ange text att kryptera: ")
förskjutning = int(input("Ange förskjutning (1-25): "))

krypterad_text = ""
alfabetet = "abcdefghijklmnopqrstuvwxyz"

for tecken in text:
    if tecken.lower() in alfabetet:
        # Hitta position i alfabetet
        position = alfabetet.index(tecken.lower())
        # Beräkna ny position med förskjutning
        ny_position = (position + förskjutning) % 26
        nytt_tecken = alfabetet[ny_position]
        
        # Behåll original case (stor/liten bokstav)
        if tecken.isupper():
            krypterad_text += nytt_tecken.upper()
        else:
            krypterad_text += nytt_tecken
    else:
        # Behåll mellanslag och skiljetecken
        krypterad_text += tecken

print(f"Krypterad text: {krypterad_text}")
print(f"För att dekryptera: använd förskjutning {26 - förskjutning}")
```

---

### Uppgift 34 – Kontaktbok

```python
kontakter = []

while True:
    print("\n=== KONTAKTBOK ===")
    print("1. Lägg till kontakt")
    print("2. Sök kontakt")
    print("3. Visa alla kontakter")
    print("4. Ta bort kontakt")
    print("5. Avsluta")
    
    val = input("Välj alternativ (1-5): ")
    
    if val == "1":
        namn = input("Namn: ")
        telefon = input("Telefon: ")
        email = input("Email: ")
        kontakter.append((namn, telefon, email))
        print("Kontakt tillagd!")
    
    elif val == "2":
        sök_namn = input("Ange namn att söka efter: ").lower()
        hittade = []
        for kontakt in kontakter:
            if sök_namn in kontakt[0].lower():
                hittade.append(kontakt)
        
        if hittade:
            print("Hittade kontakter:")
            for namn, telefon, email in hittade:
                print(f"{namn} - {telefon} - {email}")
        else:
            print("Ingen kontakt hittades.")
    
    elif val == "3":
        if len(kontakter)>0:
            # Sortera alfabetiskt
            sorterade_kontakter = sorted(kontakter)
            print("Alla kontakter (alfabetisk ordning):")
            for namn, telefon, email in sorterade_kontakter:
                print(f"{namn} - {telefon} - {email}")
        else:
            print("Inga kontakter sparade.")
    
    elif val == "4":
        namn_att_ta_bort = input("Ange namn på kontakt att ta bort: ")
        borttagen = False
        for i in range(len(kontakter)):
            if kontakter[i][0].lower() == namn_att_ta_bort.lower():
                kontakter.pop(i)
                print("Kontakt borttagen!")
                borttagen = True
                break
        
        if not borttagen:
            print("Kontakt hittades inte.")
    
    elif val == "5":
        print("Avslutar kontaktbok...")
        break
    
    else:
        print("Ogiltigt val, försök igen.")
```
