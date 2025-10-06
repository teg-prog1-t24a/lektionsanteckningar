# Övningsuppgifter - Dictionaries och Lista-konverteringar

## E-uppgifter

### Uppgift 1 – Enkel ordbok

Skapa en dictionary med tre länder som nycklar och deras huvudstäder som värden. Skriv ut hela dictionary:n.

---

### Uppgift 2 – Hämta värde

Skapa en dictionary med tre djur och deras ljud (t.ex. "katt": "mjau"). Låt användaren skriva in ett djur och skriv ut vilket ljud det gör.

---

### Uppgift 3 – Lägg till värde

Skapa en tom dictionary. Lägg till tre olika frukter som nycklar med deras färger som värden. Skriv ut dictionary:n.

---

### Uppgift 4 – Längden på en dictionary

Skapa en dictionary med fem olika fordon och deras hastighet. Skriv ut hur många fordon som finns i dictionary:n.

---

### Uppgift 5 – Alla nycklar

Skapa en dictionary med fyra olika kurser och deras poäng. Skriv ut alla kursnamn (nycklarna) på separata rader.

---

### Uppgift 6 – Alla värden

Skapa en dictionary med tre vänner och deras åldrar. Skriv ut alla åldrar (värdena) på separata rader.

---

### Uppgift 7 – Uppdatera värde

Skapa en dictionary med tre böcker och deras författare. Ändra författaren för en av böckerna och skriv ut den uppdaterade dictionary:n.

---

### Uppgift 8 – Lista till dictionary

Skapa en lista med tre namn: `["Anna", "Bert", "Cilla"]`. Gör om den till en dictionary där namnen är nycklar och värdena är längden på varje namn.

---

### Uppgift 9 – Dictionary till lista (nycklar)

Skapa en dictionary med fyra städer och deras länder. Gör om nycklarna till en lista och skriv ut listan.

---

### Uppgift 10 – Dictionary till lista (värden)

Skapa en dictionary med tre månader och antal dagar i varje månad. Gör om värdena till en lista och skriv ut listan.

---

## C-uppgifter

### Uppgift 11 – Kontrollera om nyckel finns

Skapa en dictionary med fem länder och deras valuta. Låt användaren skriva in ett land och kontrollera om landet finns i dictionary:n. Skriv ut lämpligt meddelande.

---

### Uppgift 12 – Räkna förekomster

Skapa en lista med ord: `["äpple", "banan", "äpple", "orange", "banan", "äpple"]`. Använd en dictionary för att räkna hur många gånger varje ord förekommer.

---

### Uppgift 13 – Betygsregister

Skapa en dictionary med fem elevers namn och deras betyg (A-F). Räkna och skriv ut hur många elever som har varje betyg.

---

### Uppgift 14 – Prisregister

Skapa en dictionary med varor och priser. Låt användaren mata in varor de vill köpa (en åt gången tills de skriver "klar"). Räkna ut och skriv ut totalkostnaden.

---

### Uppgift 15 – Inverterad dictionary

Skapa en dictionary med tre personer och deras favoritfärg. Skapa en ny dictionary där färgerna är nycklar och personerna är värden.

---

### Uppgift 16 – Slå samman dictionaries

Skapa två dictionaries med olika måltider och deras kalorier. Slå samman dem till en enda dictionary och skriv ut resultatet.

---

### Uppgift 17 – Filtrera dictionary

Skapa en dictionary med tio olika produkter och deras priser. Skapa en ny dictionary som endast innehåller produkter som kostar mer än 100 kr.

---

### Uppgift 18 – Lista med dictionaries

Skapa en lista som innehåller tre dictionaries. Varje dictionary ska representera en person med namn, ålder och stad. Skriv ut informationen för alla personer.

---

### Uppgift 19 – Gruppera efter värde

Skapa en dictionary med tio personers namn och deras födelseår. Gruppera personerna efter vilket årtionde de är födda i (1990-talet, 2000-talet etc.).

---

### Uppgift 20 – Vanligaste värdet

Skapa en dictionary med elevers namn och deras favoritämne. Hitta vilket ämne som är mest populärt och skriv ut det.

---

### Uppgift 21 – Dictionary från text

Ta en text (mening) och skapa en dictionary som räknar hur många gånger varje bokstav förekommer. Ignorera mellanslag och skiljetecken.

---

## A-uppgifter

### Uppgift 22 – Telefonbok med funktioner

Skapa ett komplett telefonboksprogram med följande funktioner:
- Lägg till kontakt (namn och telefonnummer)
- Sök efter kontakt
- Ta bort kontakt
- Visa alla kontakter
- Uppdatera telefonnummer
Använd en dictionary för att lagra kontakterna och skapa en meny som låter användaren välja vad de vill göra.

---

### Uppgift 23 – Ordfrekvensanalys

Skapa ett program som analyserar en längre text:
- Läs in en text från användaren eller en fil
- Räkna frekvensen av varje ord (ignorera stor/liten bokstav)
- Visa de 10 vanligaste orden
- Visa totalt antal unika ord
- Låt användaren söka efter specifika ord och visa deras frekvens

---

### Uppgift 24 – Studentregister

Skapa ett avancerat studentregister där varje student har flera betyg i olika ämnen:
- Använd nästlade dictionaries (student -> ämne -> betyg)
- Lägg till nya studenter och betyg
- Beräkna medelbetyg för varje student
- Hitta bästa student per ämne
- Visa statistik över alla betyg
- Exportera data till en lista av dictionaries

---

### Uppgift 25 – Lagerhanteringssystem

Skapa ett lagerhanteringssystem med dictionaries:
- Produkter med information: namn, pris, antal i lager, kategori
- Funktioner för att lägga till/ta bort produkter
- Sök produkter efter kategori eller prisintervall
- Kontrollera vilka produkter som börjar ta slut (< 5 st)
- Beräkna totalt lagervärde
- Hantera inköp och försäljning som uppdaterar lagret

---

## Tips och hjälpfunktioner

### Grundläggande dictionary-syntax:
```python
# Skapa dictionary
min_dict = {"nyckel1": "värde1", "nyckel2": "värde2"}

# Komma åt värde
värde = min_dict["nyckel1"]

# Lägg till/uppdatera
min_dict["ny_nyckel"] = "nytt_värde"

# Ta bort
del min_dict["nyckel1"]

# Kontrollera om nyckel finns
if "nyckel1" in min_dict:
    print("Finns!")
```

### Iterera över dictionary:
```python
# Endast nycklar
for nyckel in min_dict:
    print(nyckel)

# Nycklar och värden
for nyckel, värde in min_dict.items():
    print(f"{nyckel}: {värde}")

# Endast värden
for värde in min_dict.values():
    print(värde)
```

### Konvertera mellan listor och dictionaries:
```python
# Lista av nycklar
nycklar = list(min_dict.keys())

# Lista av värden
värden = list(min_dict.values())

# Skapa dictionary från två listor
nycklar = ["a", "b", "c"]
värden = [1, 2, 3]
ny_dict = dict(zip(nycklar, värden))

# Dictionary comprehension
ny_dict = {x: x**2 for x in range(5)}
```

### Vanliga dictionary-metoder:
- `.keys()` - alla nycklar
- `.values()` - alla värden
- `.items()` - alla nyckel-värde par
- `.get(nyckel, default)` - hämta värde med fallback
- `.pop(nyckel)` - ta bort och returnera värde
- `.update(annan_dict)` - slå samman dictionaries

### Nästlade strukturer:
```python
# Dictionary med listor som värden
studenter = {
    "Anna": [85, 92, 78],
    "Bert": [90, 88, 95]
}

# Lista med dictionaries
personer = [
    {"namn": "Anna", "ålder": 25},
    {"namn": "Bert", "ålder": 30}
]

# Dictionary med dictionaries
skola = {
    "Anna": {"ålder": 25, "betyg": {"Matte": "A", "Svenska": "B"}},
    "Bert": {"ålder": 30, "betyg": {"Matte": "B", "Svenska": "A"}}
}
```

### Felsökning:
- Använd `print()` för att kontrollera dictionary-innehåll
- Kom ihåg att dictionary-nycklar är case-sensitive
- Använd `.get()` istället för `[]` för att undvika KeyError
- Kontrollera datatyper - nycklar måste vara oföränderliga (strängar, tal, tuples)

### Designprinciper:
- Välj beskrivande nyckelnamn
- Håll datastrukturen så enkel som möjligt
- Tänk på prestanda - dictionaries är snabba för uppslagning
