# Övningsuppgifter - Funktioner

## E-uppgifter

### Uppgift 1 – Enkel funktion

Skriv en funktion som heter `hälsa()` som skriver ut "Hej världen!" när den anropas. Anropa funktionen.

---

### Uppgift 2 – Funktion med parameter

Skriv en funktion som heter `hälsa_person(namn)` som tar emot ett namn som parameter och skriver ut "Hej [namn]!". Anropa funktionen med ditt eget namn.

---

### Uppgift 3 – Enkel returvärde

Skriv en funktion som heter `dubbla(tal)` som tar emot ett tal och returnerar talet multiplicerat med 2. Testa funktionen genom att anropa den med olika tal.

---

### Uppgift 4 – Addition

Skriv en funktion som heter `addera(tal1, tal2)` som tar emot två tal och returnerar summan. Anropa funktionen och skriv ut resultatet.

---

### Uppgift 5 – Kvadrat

Skriv en funktion som heter `kvadrat(tal)` som beräknar och returnerar kvadraten av ett tal. Testa med några olika tal.

---

### Uppgift 6 – Slumpmässigt tal

Skriv en funktion som heter `slumptal()` som returnerar ett slumpmässigt tal mellan 1 och 10. Anropa funktionen flera gånger.

---

### Uppgift 7 – Versaler funktion

Skriv en funktion som heter `skriv_högt(text)` som tar emot en text och skriver ut den i versaler med ett utropstecken.

---

### Uppgift 8 – Är jämnt

Skriv en funktion som heter `är_jämnt(tal)` som returnerar `True` om talet är jämnt, annars `False`.

---

### Uppgift 9 – Största talet

Skriv en funktion som heter `största(tal1, tal2)` som returnerar det största av två tal.

---

### Uppgift 10 – Personlig presentation

Skriv en funktion som heter `presentera(namn, ålder)` som tar emot namn och ålder och skriver ut "Jag heter [namn] och är [ålder] år gammal."

---

### Uppgift 11 – Cirkelns area

Skriv en funktion som heter `cirkel_area(radie)` som beräknar och returnerar arean av en cirkel. Använd `math.pi`.

---

### Uppgift 12 – Temperaturomvandling

Skriv en funktion som heter `celsius_till_fahrenheit(celsius)` som omvandlar Celsius till Fahrenheit och returnerar resultatet.

---

## C-uppgifter

### Uppgift 13 – Kasta tärning flera gånger

Skriv en funktion `kasta_tärningar(antal)` som kastar ett angivet antal tärningar (tal mellan 1-6) och returnerar en lista med resultaten.

---

### Uppgift 14 – Medelvärdeskalkylator

Skriv en funktion `medelvärde(lista)` som tar emot en lista med tal och returnerar medelvärdet. Testa med olika listor.

---

### Uppgift 15 – Faktorial

Skriv en funktion `faktorial(n)` som beräknar och returnerar faktorialen av ett tal (n! = n × (n-1) × (n-2) × ... × 1).

---

### Uppgift 16 – Kontrollera primtal

Skriv en funktion `är_primtal(tal)` som kontrollerar om ett tal är ett primtal och returnerar `True` eller `False`.

---

### Uppgift 17 – Stränganalys

Skriv en funktion `analysera_sträng(text)` som returnerar en tuple med (antal_tecken, antal_ord, antal_vokaler).

---

### Uppgift 18 – Lista med villkor

Skriv en funktion `filtrera_jämna(lista)` som tar emot en lista med tal och returnerar en ny lista med endast de jämna talen.

---

### Uppgift 19 – Lösenordsgenerator

Skriv en funktion `generera_lösenord(längd)` som genererar och returnerar ett slumpmässigt lösenord med angiven längd (använd bokstäver och siffror).

---

### Uppgift 20 – Betygskonvertering

Skriv en funktion `poäng_till_betyg(poäng)` som konverterar poäng (0-100) till betyg (F, E, D, C, B, A) och returnerar betyget.

---

### Uppgift 21 – Räkna ord

Skriv en funktion `räkna_ord(text, sökord)` som räknar hur många gånger ett specifikt ord förekommer i en text.

---

### Uppgift 22 – Geometriska former

Skriv funktioner för att beräkna area och omkrets för:
- `rektangel_area(längd, bredd)`
- `rektangel_omkrets(längd, bredd)`
- `triangel_area(bas, höjd)`

Testa alla funktioner.

---

### Uppgift 23 – Validering av input

Skriv en funktion `validera_ålder(ålder_str)` som kontrollerar om en sträng är en giltig ålder (heltal mellan 0-120). Returnera `True/False`.

---

### Uppgift 24 – Fibonacci-tal

Skriv en funktion `fibonacci(n)` som returnerar det n:te talet i Fibonacci-serien.

---

## A-uppgifter

**Obs! Svårigheterna i flera av A-uppgifterna i det här avsnittet är snarare att de är längre och involverar mer kod som skall fungera tillsammans än att själva koden är svårare.**

Uppgifterna tar betydligt längre tid att lösa. Många är för omfattande för att fungera väl i en _provsituation_ men de hjälper dig att lära dig så att du också klarar av kortare svåra uppgifter.

Mitt tips är att välja 1-2 och göra dem noggrant. Titta på lösningsförslagen och försök förstå hur den lösningen fungerar. Det finns många olika sätt att skriva de här programmen.

### Uppgift 25 – Enkel kalkylator

Skapa en kalkylator med funktioner för grundläggande operationer:
- `addera(a, b)`, `subtrahera(a, b)`, `multiplicera(a, b)`, `dividera(a, b)`
- En huvudfunktion `kalkylator()` som låter användaren välja operation och mata in tal
- Hantera division med noll

---

### Uppgift 26 – Textanalysverktyg

Skapa ett textanalysverktyg med flera funktioner:
- `räkna_tecken(text)` - räknar totala antalet tecken
- `räkna_ord(text)` - räknar antalet ord  
- `vanligaste_ord(text)` - hittar det vanligaste ordet - vi kan inte göra det här på ett effektivt sätt än men vi KAN göra det om vi är lite kluriga
- `omvänd_text(text)` - vänder texten baklänges
- En huvudfunktion som låter användaren välja vilken analys de vill göra

---

### Uppgift 27 – Bankonto-simulator

Skapa funktioner för att simulera ett bankkonto:
- `skapa_konto(startbelopp)` - returnerar kontobalans
- `sätt_in(balans, belopp)` - lägger till pengar
- `ta_ut(balans, belopp)` - tar ut pengar (kontrollera att det finns tillräckligt)
- `visa_balans(balans)` - visar nuvarande balans
- `ränta(balans, räntesats)` - beräknar och lägger till ränta
- En huvudfunktion som simulerar banktransaktioner

---

### Uppgift 28 – Spel: Gissa numret (avancerat)

Skapa ett avancerat "gissa numret"-spel:
- `välj_svårighetsgrad()` - låter spelaren välja intervall
- `generera_hemligt_tal(min_val, max_val)` - skapar det hemliga talet
- `få_gissning()` - tar emot och validerar spelarens gissning
- `ge_tips(gissning, hemligt_tal)` - ger ledtrådar
- `spela_spel()` - huvudfunktionen som kör hela spelet
- Håll koll på antal gissningar och ge olika meddelanden baserat på prestationen

---

### Uppgift 29 – Elevregister

Skapa ett system för att hantera elever och betyg:
- `lägg_till_elev(register, namn)` - lägger till en elev i registret (använd lista av listor)
- `lägg_till_betyg(register, namn, ämne, betyg)` - lägger till betyg för en elev
- `beräkna_medelbetyg(register, namn)` - beräknar medelbetyg för en elev
- `hitta_bästa_elev(register)` - hittar eleven med högsta medelbetyget
- `visa_alla_elever(register)` - visar alla elever och deras betyg
- En huvudfunktion som låter användaren hantera registret

---

### Uppgift 30 – Enkel kryptografi

Implementera Caesar-kryptering med funktioner:
- `kryptera_bokstav(bokstav, förskjutning)` - krypterar en enskild bokstav
- `kryptera_text(text, förskjutning)` - krypterar en hel text
- `dekryptera_text(krypterad_text, förskjutning)` - dekrypterar text
- `knäck_kod(krypterad_text)` - försöker knäcka koden genom att testa alla förskjutningar
- En huvudfunktion som låter användaren välja operation

---

## Tips och hjälpfunktioner

### Grundläggande funktionssyntax:
```python
def funktionsnamn(parameter1, parameter2):
    # kod här
    return resultat  # (valfritt)
```

### Användbara imports för uppgifterna:
```python
import random      # för slumpmässiga tal
import math        # för matematiska funktioner
import string      # för bokstäver och tecken
```

### Vanliga funktioner att känna till:
- `random.randint(a, b)` - slumpmässigt heltal mellan a och b
- `random.choice(lista)` - väljer slumpmässigt element från lista
- `math.pi` - konstanten pi
- `math.sqrt(x)` - kvadratrot
- `string.ascii_letters` - alla bokstäver
- `string.digits` - alla siffror

### Designprinciper för funktioner:
- En funktion bör göra en sak och göra den bra
- Använd beskrivande namn
- Funktioner med returvärden är ofta mer användbara än de som bara skriver ut
- Validera input när det behövs
- Kommentera komplicerade funktioner

### Testning av funktioner:
```python
# Testa alltid dina funktioner med olika värden
print(min_funktion(5))    # normalt fall
print(min_funktion(0))    # kantfall
print(min_funktion(-3))   # negativt tal
```

### Felsökning:
- Använd `print()` inuti funktioner för att se vad som händer
- Kontrollera att du returnerar rätt datatyp
- Se till att alla kodvägar returnerar något (om funktionen ska returnera något)
- Testa funktioner separat innan du använder dem i större program
