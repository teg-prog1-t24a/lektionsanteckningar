# Extra A-uppgifter - Funktioner
 
---

## Uppgift 1 – Palindrom-kontrollare

Skriv en funktion som kontrollerar om en text är ett palindrom (läses likadant framåt och bakåt).

**Krav:**
- Ignorera mellanslag och skiljetecken
- Ignorera stor/liten bokstav
- Returnera `True` eller `False`

**Exempel:**
- `"Anna"` → `True`
- `"Ni talar bra latin"` → `True`  
- `"A man a plan a canal Panama"` → `True`
- `"Hej"` → `False`

Testa med minst 3 olika exempel.

---

## Uppgift 2 – Lösenordsvalidering

Skapa ett system för att validera lösenord. Du behöver flera funktioner som arbetar tillsammans. En sådan kan till exempel
heta `innehåller_siffra(text)`.

**Ett starkt lösenord ska:**
- Vara minst 8 tecken långt
- Innehålla minst en siffra
- Innehålla minst en stor bokstav
- Innehålla minst en liten bokstav

**Testa med dessa lösenord:**
- `"hejsan123"` (svagt - ingen stor bokstav)
- `"HEJSAN123"` (svagt - ingen liten bokstav)  
- `"Hej123"` (svagt - för kort)
- `"Hej12345"` (starkt)
- `"HejAllihopa"` (svagt - ingen siffra)

Skriv ut om varje lösenord är starkt eller svagt och varför.

---

## Uppgift 3 – Talanalys

Skapa funktioner för att analysera en lista med tal och skriva ut en komplett rapport.

**Din rapport ska innehålla:**
- Minsta och största värde
- Antal jämna och udda tal
- Medelvärde
- Median (mittersta värdet när talen är sorterade)

**Tips för median:** Sortera listan först. Om listan har udda antal element, ta det mittersta. Om den har jämnt antal element, ta medelvärdet av de två mittersta. Använd `list.sort()` eller `sorted`.

**Testa med:** `[4, 2, 8, 1, 9, 3, 7, 5, 6]`

**Exempel på utskrift:**
```
=== TALANALYS ===
Lista: [4, 2, 8, 1, 9, 3, 7, 5, 6]
Minsta värde: 1
Största värde: 9
Antal jämna tal: 4
Antal udda tal: 5
Medelvärde: 5.0
Median: 5
```

---

## Uppgift 4 – Anagram-detektor

Skapa funktioner för att arbeta med anagram (ord som består av samma bokstäver i olika ordning).

**Vad du ska göra:**
1. Kontrollera om två ord är anagram av varandra
2. I en lista av ord, hitta alla som är anagram till ett givet ord

**Testa med:**
- Ordlista: `["lager", "regal", "mark", "kram", "kastet", "takets", "staket", "regla"]`
- Målord: `"lager"`

**Tips:** Två ord är anagram om de innehåller exakt samma bokstäver. Tänk på hur du kan jämföra detta enkelt.

**Förväntad utskrift:**
```
Anagram till 'lager': ['regal', 'regla']
```

---

## Uppgift 5 – Textformattering

Skapa funktioner för att analysera och formatera text på olika sätt.

**Vad du ska göra:**
1. Beräkna längden på varje ord i texten
2. Hitta det längsta ordet
3. Skapa en akronym (första bokstaven i varje ord)
4. Formatera texten så den får radbrytningar vid en viss bredd

**För formateringen:** Lägg ord på samma rad tills nästa ord inte får plats, då bryt rad och fortsätt.

**Testa med:**
- Text: `"Python är ett fantastiskt programmeringsspråk för nybörjare"`  
- Bredd: 20 tecken

**Förväntad utskrift:**
```
Ordlängder: [6, 2, 3, 11, 18, 3, 10]
Längsta ord: programmeringsspråk
Akronym: PAEFPFN

Formaterad text (bredd 20):
Python är ett
fantastiskt
programmeringsspråk
för nybörjare
```

---

## Tips för alla uppgifter

### Allmänna råd:
- Börja med att planera vilka funktioner du behöver
- Skriv en funktion i taget och testa den
- Använd beskrivande funktionsnamn
- Kommentera komplicerad kod

### Användbara tekniker:
- `text.lower()` - gör om till små bokstäver
- `text.replace(" ", "")` - tar bort mellanslag
- `sorted(lista)` - sorterar en lista
- `ord("a")` och `chr(97)` - konverterar mellan bokstäver och siffror
- `len(lista) // 2` - hittar mitten av en lista

### Testning:
- Testa alltid dina funktioner med olika värden
- Tänk på kantfall (tomma strängar, negativa tal, etc.)
- Skriv ut mellanresultat om något inte fungerar
