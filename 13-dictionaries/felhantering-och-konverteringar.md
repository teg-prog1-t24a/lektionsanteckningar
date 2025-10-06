# Övningsuppgifter - Felhantering och Datakonverteringar

## E-uppgifter

### Uppgift 1 – Enkel felhantering

Skriv ett program som frågar användaren efter ett tal. Använd `try...except` för att hantera fallet då användaren skriver något som inte är ett tal. Skriv ut ett felmeddelande om det går fel.

---

### Uppgift 2 – Split en mening

Skapa en sträng med en mening (minst 5 ord). Använd `split()` för att dela upp meningen i ord och skriv ut varje ord på en egen rad.

---

### Uppgift 3 – Join en lista

Skapa en lista med fyra ord: `["Jag", "älskar", "att", "programmera"]`. Använd `join()` för att slå samman dem till en mening och skriv ut resultatet.

---

### Uppgift 4 – Sträng till lista

Ta en sträng som innehåller namn separerade med komma: `"Anna,Bert,Cilla,David"`. Konvertera den till en lista med namn och skriv ut listan.

---

### Uppgift 5 – Lista till sträng

Skapa en lista med tal: `[1, 2, 3, 4, 5]`. Konvertera alla tal till strängar och slå samman dem med bindestreck mellan. Resultatet ska bli `"1-2-3-4-5"`.

---

### Uppgift 6 – Sträng till tecken-lista

Ta en sträng, t.ex. `"Python"`. Konvertera den till en lista med varje tecken separat och skriv ut listan.

---

### Uppgift 7 – Säker division

Skriv ett program som frågar användaren efter två tal och dividerar dem. Använd `try...except` för att hantera division med noll och ogiltiga tal.

---

### Uppgift 8 – Dictionary lookup med felhantering

Skapa en dictionary med några länder och huvudstäder. Låt användaren söka efter ett land. Använd `try...except` för att hantera när landet inte finns, alternativt använd `.get()` metoden.

---

### Uppgift 9 – Lista från input

Låt användaren skriva in flera tal separerade med mellanslag (t.ex. "1 2 3 4 5"). Konvertera input till en lista med heltal och beräkna summan.

---

### Uppgift 10 – Join med olika separator

Skapa en lista med städer: `["Stockholm", "Göteborg", "Malmö"]`. Använd `join()` för att skapa:
a) En sträng med städerna separerade med ", "
b) En sträng med städerna separerade med " -> "

---

## C-uppgifter

### Uppgift 11 – Robust talkonvertering

Skapa en funktion som tar emot en sträng och försöker konvertera den till ett tal (int eller float). Funktionen ska returnera talet om det går, annars `None`. Testa funktionen med olika input.

---

### Uppgift 12 – CSV-parser

Skapa en sträng som representerar CSV-data: `"Namn,Ålder,Stad\nAnna,25,Stockholm\nBert,30,Göteborg"`. Använd `split()` för att:
- Dela upp raderna
- Dela upp kolumnerna
- Skapa en lista med dictionaries för varje person

---

### Uppgift 13 – Säker lista-access

Skapa en lista med fem element. Låt användaren mata in ett index. Använd `try...except` för att säkert komma åt elementet på det indexet. Hantera både ogiltiga index och icke-numerisk input.

---

### Uppgift 14 – Textanalys med split

Ta en längre text (flera meningar). Använd olika `split()`-metoder för att:
- Räkna antal meningar (split på ".")
- Räkna antal ord (split på mellanslag)
- Hitta alla ord som börjar med en viss bokstav

---

### Uppgift 15 – Formaterad utskrift

Skapa en lista med dictionaries som representerar produkter (namn, pris, antal). Använd `join()` för att skapa en snygg tabell-utskrift av all produktinformation.

---

### Uppgift 16 – Säker dictionary-operationer

Skapa ett program som låter användaren:
- Lägga till nycklar och värden i en dictionary
- Söka efter nycklar
- Ta bort nycklar
Hantera alla möjliga fel som kan uppstå och ge användarvänliga felmeddelanden.

---

### Uppgift 17 – Data-rensning

Ta en lista med "smutsig" data: `["123", "abc", "45.6", "", "null", "789"]`. Använd felhantering för att:
- Konvertera alla giltiga tal till float
- Räkna hur många värden som inte kunde konverteras
- Skapa en ren lista med endast talen

---

### Uppgift 18 – Avancerad split och join

Ta en text som innehåller flera typer av separatorer: `"äpple;banan,orange:päron;grape"`. Skapa en funktion som kan dela upp texten på flera olika separatorer och returnera en ren lista med ord.

---

### Uppgift 20 – Backup-konvertering

Skapa en funktion som försöker konvertera en sträng till heltal, men om det misslyckas, försöker konvertera till float, och om det också misslyckas returnerar strängen som den är.

---

## Tips och hjälpfunktioner

### Try...except syntax:
```python
try:
    # Kod som kan ge fel
    resultat = int(input("Ange ett tal: "))
except ValueError:
    print("Det var inte ett giltigt tal!")
except Exception as e:
    print(f"Något gick fel: {e}")
else:
    print("Allt gick bra!")
finally:
    print("Detta körs alltid")
```

### Split och join:
```python
# Split
text = "äpple,banan,orange"
lista = text.split(",")           # ['äpple', 'banan', 'orange']
ord = "hello world".split()       # ['hello', 'world']
rader = text.split("\n")          # Dela på rader

# Join
lista = ["a", "b", "c"]
text = ",".join(lista)            # "a,b,c"
text = " -> ".join(lista)         # "a -> b -> c"
```

### Vanliga konverteringar:
```python
# Sträng till lista av tecken
lista = list("hello")             # ['h', 'e', 'l', 'l', 'o']

# Lista av tal till sträng
tal = [1, 2, 3, 4]
text = ",".join(map(str, tal))    # "1,2,3,4"

# Sträng till lista av tal
text = "1 2 3 4"
tal = [int(x) for x in text.split()]  # [1, 2, 3, 4]
```

### Vanliga fel att hantera:
- `ValueError` - fel vid konvertering (int("abc"))
- `KeyError` - nyckel finns inte i dictionary
- `IndexError` - index utanför lista
- `ZeroDivisionError` - division med noll
- `TypeError` - fel datatyp för operation

### Säkra alternativ:
```python
# Istället för dict[key]
värde = dict.get(key, "default")

# Istället för int(sträng)
try:
    tal = int(sträng)
except ValueError:
    tal = 0  # eller något standardvärde

# Kontrollera index
if 0 <= index < len(lista):
    element = lista[index]
```

### Debugging tips:
- Använd `print()` för att se vad som händer
- Testa med olika typer av fel input
- Läs felmeddelanden noggrant
- Använd specifika except-klausuler istället för bara `except:`
- Logga fel för senare analys

### Best practices:
- Fånga specifika fel, inte alla fel
- Ge användarvänliga felmeddelanden
- Validera input tidigt
- Ha fallback-värden när det är lämpligt
- Dokumentera vilka fel som kan uppstå