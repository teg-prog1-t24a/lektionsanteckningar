# Blandade övningsuppgifter - Repetition

## E-uppgifter

### Uppgift 1 – Grundläggande variabler

Skapa två variabler: en för ditt namn (sträng) och en för din ålder (heltal). Skriv ut båda med hjälp av en f-sträng.

---

### Uppgift 2 – Enkel aritmetik

Låt användaren mata in två tal. Räkna ut och skriv ut summan, skillnaden och produkten av talen.

---

### Uppgift 3 – Jämförelse

Skapa två variabler med olika tal. Använd jämförelseoperatorer för att skriva ut om det första talet är större än, mindre än eller lika med det andra.

---

### Uppgift 4 – Enkelt villkor

Låt användaren mata in sin ålder. Om åldern är 18 eller mer, skriv ut "Du får rösta". Annars skriv ut "Du får inte rösta än".

---

### Uppgift 5 – Strängindexering

Skapa en sträng med ditt namn. Skriv ut den första och sista bokstaven i namnet.

---

### Uppgift 6 – Lista med tal

Skapa en lista med fem heltal. Skriv ut listan och dess längd.

---

### Uppgift 7 – Tuple med koordinater

Skapa en tuple med x- och y-koordinater. Skriv ut koordinaterna på formatet "x: 5, y: 3".

---

### Uppgift 8 – Enkel loop

Använd en for-loop för att skriva ut alla tal från 1 till 5.

---

### Uppgift 9 – Typkonvertering

Låt användaren mata in ett tal som sträng. Konvertera det till ett heltal och skriv ut det multiplicerat med 2.

---

### Uppgift 10 – Strängmetod

Skapa en sträng med blandat stora och små bokstäver. Skriv ut strängen i versaler och gemener.

---

### Uppgift 11 – While-loop

Använd en while-loop för att skriva ut alla jämna tal från 2 till 10.

---

### Uppgift 12 – Lista med strängar

Skapa en lista med tre städer. Skriv ut varje stad med hjälp av en for-loop.

---

## C-uppgifter

### Uppgift 13 – Gissa talet

Skapa ett program där datorn "tänker" på ett tal mellan 1 och 10 (använd `random.randint()`). Låt användaren gissa och säg om gissningen är rätt eller fel.

---

### Uppgift 14 – Faktorisering

Låt användaren mata in ett heltal. Skriv ut alla faktorer av det talet (tal som delar talet utan rest).

---

### Uppgift 15 – Medelvärde från input

Låt användaren mata in tre tal. Beräkna och skriv ut medelvärdet med två decimaler. (Tips: använd `round()` eller läs på om f-strängar och formattering).

---

### Uppgift 16 – Sträng-analys

Låt användaren mata in ett ord. Skriv ut:
- Ordets längd
- Ordet baklänges  
- Antal vokaler (a, e, i, o, u, y, å, ä, ö)

---

### Uppgift 17 – List-manipulation

Skapa en tom lista. Låt användaren mata in fem tal och lägg till dem i listan med `append()`. Skriv sedan ut:
- Hela listan
- Största och minsta talet
- Summan av alla tal

---

### Uppgift 18 – Multiplikationstabell

Låt användaren mata in ett tal. Skriv ut multiplikationstabellen för det talet (1-10).

---

### Uppgift 19 – Tuple unpacking

Skapa en lista med tuples som innehåller namn och ålder för tre personer. Använd tuple unpacking för att skriva ut varje persons information på formatet "Namn är X år gammal".

---

### Uppgift 20 – Villkor med logiska operatorer

Låt användaren mata in ett tal. Kontrollera om talet är:
- Positivt OCH jämnt
- Negativt ELLER större än 100
- INTE lika med 0

Skriv ut resultatet för varje kontroll.

---

### Uppgift 21 – Slicing och bearbetning

Skapa en sträng med minst 10 tecken. Använd slicing för att:
- Ta ut de första tre tecknen
- Ta ut de sista tre tecknen  
- Ta ut vartannat tecken från hela strängen

---

### Uppgift 22 – Nästlade villkor

Låt användaren mata in ett årtal. Kontrollera om året är ett skottår enligt följande regler:
- Året är delbart med 4
- Om året är delbart med 100, måste det också vara delbart med 400 för att vara ett skottår
- Skriv ut om året är ett skottår eller inte

---

### Uppgift 23 – Lista med villkor

Skapa en lista med tio slumpmässiga tal mellan 1 och 20. Räkna och skriv ut:
- Hur många tal som är större än 10
- Hur många tal som är jämna

---

### Uppgift 24 – Break i loop

Skapa ett program som frågar användaren efter tal tills de skriver "stopp". Skriv ut summan av alla inmatade tal.

---

## A-uppgifter

### Uppgift 25 – Lösenordsvalidering

Skapa ett program som kontrollerar om ett lösenord är starkt. Ett starkt lösenord ska:
- Vara minst 8 tecken långt
- Innehålla minst en siffra
- Innehålla minst en stor bokstav
- Innehålla minst en liten bokstav

Skriv ut om lösenordet är starkt eller svagt och vilka krav som saknas.

---

### Uppgift 26 – Anagram-detektor

Skapa ett program som kontrollerar om två ord är anagram (innehåller samma bokstäver i olika ordning). Till exempel: "listen" och "silent".

---

### Uppgift 27 – Enkel statistik

Låt användaren mata in tal tills de skriver "klar". Beräkna och skriv ut:
- Antal tal som matades in
- Medelvärde
- Största och minsta talet  
- Hur många tal som var över medelvärdet

---

### Uppgift 28 – Matris-operationer

Skapa en 3x3 matris (lista av listor) med slumpmässiga tal mellan 1 och 9. Skriv ut:
- Hela matrisen i ett snyggt format
- Summan av varje rad
- Summan av varje kolumn
- Summan av diagonal (från övre vänster till nedre höger)

---

### Uppgift 29 – Ordfrekvens

Låt användaren mata in en mening. Skapa ett program som räknar hur många gånger varje ord förekommer och presenterar resultatet sorterat efter frekvens.

Tips:
- läs på om och använd funktionen `split()`
- använd dubbla loopar (senare lär vi oss att använda dictionaries för detta)
- läs på om och använd `sorted()` för att sortera resultatet (valfritt)

---

### Uppgift 30 – Fibonacci-sekvens

Skapa ett program som genererar Fibonacci-sekvensen upp till ett visst antal termer som användaren anger. Spara sekvensen i en lista och skriv ut den.

---

### Uppgift 31 – Primtals-detektor med lista

Skapa ett program som:
1. Låter användaren mata in ett tal
2. Kontrollerar om talet är ett primtal
3. Om det inte är ett primtal, visa alla dess delare
4. Sparar alla primtal som testats i en lista och visar den

---

### Uppgift 32 – Tärningsspel

Skapa ett enkelt tärningsspel för två spelare:
- Varje spelare kastar en tärning (slumpmässigt tal 1-6)
- Den som får högst vinner omgången
- Spela 5 omgångar och håll koll på poängen
- Skriv ut vinnaren av hela spelet
- Visa statistik för varje spelare (antal vinster, genomsnittskast)

---

### Uppgift 33 – Text-kryptering

Implementera en enkel Caesar-kryptering:
- Låt användaren mata in en text och en förskjutning (1-25)
- Kryptera texten genom att förskjuta varje bokstav i alfabetet
- Behåll mellanslag och skiljetecken oförändrade
- Visa både den krypterade texten och hur man dekrypterar den

---

### Uppgift 34 – Kontaktbok

Skapa en enkel kontaktbok:
- Använd en lista av tuples för att lagra kontakter (namn, telefon, email)
- Låt användaren lägga till nya kontakter
- Implementera sökning efter namn
- Visa alla kontakter i alfabetisk ordning
- Låt användaren ta bort kontakter

---

## Tips och hjälpfunktioner

### Användbara funktioner:
- `input()` - för användarinmatning
- `print()` - för utskrift
- `len()` - längd på strängar, listor, tuples
- `range()` - för att skapa talsekvenser i loopar
- `int()`, `float()`, `str()` - typkonvertering
- `random.randint(a, b)` - slumpmässigt heltal mellan a och b
- `sum()`, `max()`, `min()` - för beräkningar på listor
- `sorted()` - för att sortera

### Användbara strängmetoder:
- `.lower()`, `.upper()` - konvertera till gemener/versaler
- `.strip()` - ta bort mellanslag i början/slutet
- `.replace(old, new)` - ersätta text
- `.split()` - dela upp sträng till lista
- `.count(substring)` - räkna förekomster
- `.find(substring)` - hitta position

### Användbara listmetoder:
- `.append(item)` - lägg till element
- `.remove(item)` - ta bort element
- `.pop()` - ta bort och returnera sista elementet
- `.count(item)` - räkna förekomster
- `.index(item)` - hitta position

### Operatorer:
- Aritmetik: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Jämförelse: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logiska: `and`, `or`, `not`
- Medlemskap: `in`, `not in`
