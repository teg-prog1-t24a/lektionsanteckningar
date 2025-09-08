# Lösningsförslag

## E-uppgifter

### Uppgift 1 – Skapa en lista

```python
frukter = ["äpple", "banan", "päron"]
print(frukter)
```

---

### Uppgift 2 – Första elementet

```python
tal = [3, 7, 12, 5, 9]
print(tal[0])
```

---

### Uppgift 3 – Längden på en lista

```python
namn = ["Anna", "Bo", "Cecilia"]
print(len(namn))
```

---

### Uppgift 4 – Slumpmässigt val ur lista

```python
import random
färger = ["röd", "blå", "grön", "gul"]
i = random.randint(0, len(färger)-1)
print(färger[i])
```

---

### Uppgift 5 – Iterera över lista

```python
djur = ["hund", "katt", "häst"]
for d in djur:
    print(d)
```

---

### Uppgift 6 – Ändra element

```python
städer = ["Stockholm", "Göteborg", "Malmö"]
städer[1] = "Uppsala"
print(städer)
```

---

### Uppgift 7 – Sista elementet

```python
ord = ["en", "två", "tre", "fyra", "fem"]
print(ord[-1])
```

---

### Uppgift 8 – Enkel tuple

```python
koord = (3, 5, 7)
print(koord)
```

---

### Uppgift 9 – Indexering i tuple

```python
ord = ("sol", "måne", "stjärna")
print(ord[1])
```

---

### Uppgift 10 – Loopa tuple

```python
siffror = (2, 4, 6, 8)
for s in siffror:
    print(s)
```

---

### Uppgift 11 – Negativt index

```python
namn = ["Anna", "Bo", "Cecilia", "David"]
print(namn[-1])
```

---

### Uppgift 12 – Slicing

```python
ord = ["ett", "två", "tre", "fyra", "fem"]
print(ord[:3])
```

---

## C-uppgifter

### Uppgift 13 – Byta plats

```python
tal = [1, 2, 3]
tal[0], tal[-1] = tal[-1], tal[0]
print(tal)
```

---

### Uppgift 14 – Kontrollera om värde finns

```python
ord = ["sol", "vind", "vatten", "eld", "is"]
sök = input("Skriv ett ord: ")
if sök in ord:
    print(f"{sök} finns i listan")
else:
    print(f"{sök} finns inte i listan")
```

---

### Uppgift 15 – Summera lista

```python
tal = [3, 6, 8, 2]
print(sum(tal))
```

---

### Uppgift 16 – Medelvärde

```python
tal = [4, 8, 15, 16, 23]
print(sum(tal) / len(tal))
```

---

### Uppgift 17 – Största talet

a)

```python
tal = [7, 2, 9, 5]
print(max(tal))
```

b)

```python
störst = tal[0]
for t in tal:
    if t > störst:
        störst = t
print(störst)
```

---

### Uppgift 18 – Räkna förekomster

```python
ord = ["äpple", "päron", "äpple", "banan", "äpple"]
print(ord.count("äpple"))
```

---

### Uppgift 19 – Slumpmässig lista

```python
import random
tal = []
for i in range(5):
    tal.append(random.randint(1, 10))
print(tal)
```

---

### Uppgift 20 – Lista till tuple

```python
lista = ["Anna", "Bo", "Cecilia"]
tupl = tuple(lista)
print(tupl)
```

---

### Uppgift 21 – Tuple till lista

```python
tupl = (1, 2, 3, 4)
lista = list(tupl)
print(lista)
```

---

### Uppgift 22 – Palindromlista

```python
ord = ["hej", "på", "dig"]
print(ord)
print(ord[::-1])
```

---

### Uppgift 23 – Mata in till lista

```python
tal = []
for i in range(1, 4):
    t = int(input(f"Mata in tal {i}: "))
    tal.append(t)
print(tal)
```

---

### Uppgift 24 – Tuple unpacking

```python
info = ("Anna", 25)
namn, ålder = info
print(f"{namn} är {ålder} år gammal")
```

---

## A-uppgifter

### Uppgift 25 – Unik i lista

```python
ord = ["a", "b", "a", "c", "d", "d"]
for o in ord:
    if ord.count(o) == 1:
        print(o)
```

---

### Uppgift 26 – Nästlad loop med lista

```python
namn = ["Anna", "Bo", "Cecilia"]
for n in namn:
    for siffra in range(1, 4):
        print(f"{n} {siffra}")
```

---

### Uppgift 27 – Hitta dubbeltal

```python
import random
tal = [random.randint(1, 5) for _ in range(10)]
print(tal)
for t in set(tal):
    if tal.count(t) > 1:
        print(t)
```

---

### Uppgift 28 – Sortera lista

a)

```python
import random
tal = [random.randint(1, 20) for _ in range(5)]
tal.sort()
print(tal)
```

b)

```python
tal = [7, 3, 12, 5, 9]
for i in range(len(tal)):
    for j in range(i+1, len(tal)):
        if tal[j] < tal[i]:
            tal[i], tal[j] = tal[j], tal[i]
print(tal)
```

---

### Uppgift 29 – Hitta gemensamma värden

```python
lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]
for tal in lista1:
    if tal in lista2:
        print(tal)
```

---

### Uppgift 30 – Tuple som koordinater

```python
punkter = [(0, 1), (2, 1), (3, 2)]
for p in punkter:
    if p[1] == 1:
        print(p)
```

---

### Uppgift 31 – List comprehension kvadrater

```python
kvadrater = [i*i for i in range(1, 11)]
print(kvadrater)
```

---

### Uppgift 32 – List comprehension jämna tal

```python
jämna = [i for i in range(0, 21) if i % 2 == 0]
print(jämna)
```

---
