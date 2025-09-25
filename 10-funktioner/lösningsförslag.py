from random import randint

# Uppgift 1
def hälsa():
    print("Hej världen!")

hälsa()

# Uppgift 2
def hälsa_person(namn):
    print(f"Hej {namn}!")

hälsa_person("Micke")

# Uppgift 3
def dubbla(tal):
    return tal*2

print(dubbla(4))
print(dubbla(16))
print(dubbla(100))

# Uppgift 4
def addera(tal1, tal2):
    return tal1 + tal2

print(addera(14,27))

# Uppgift 5
def kvadrat(tal):
    return tal**2

print(kvadrat(12))
print(kvadrat(-5))

# Uppgift 6
def slumptal():
    return randint(1,10)

print(slumptal())
print(slumptal())
print(slumptal())
print(slumptal())

# Uppgift 7
def skriv_högt(text):
    print(f"{text.upper()}!")

# Uppgift 8
def är_jämnt(tal):
    if tal%2==0:
        return True
    else:
        return False

# eller lite snyggare
def är_jämnt2(tal):
    return tal%2==0

# Uppgift 9
def största(tal1, tal2):
    if tal1>tal2:
        return tal1
    else:
        return tal2

# Uppgift 10

def presentera(namn, ålder):
    print(f"Jag heter {namn} och är {ålder} år gammal.")

presentera("Micke", 50)

# Uppgift 11

import math
def cirkel_area(radie):
    return math.pi*radie*radie

# Uppgift 12

def celsius_till_farenheit(celsius):
    return celsius*9/5 + 32

print(celsius_till_farenheit(37))
print(celsius_till_farenheit(37))
print(celsius_till_farenheit(37))

# Uppgift 13
def kasta_tärningar(antal):
    lst = []
    # När loopvariabeln inte används
    # brukar vi kalla den för _
    for _ in range(antal):
        tärning = randint(1,6)
        lst.append(tärning)
    return lst

print(kasta_tärningar(3))
print(kasta_tärningar(5))

# eller lite snyggare med
# list comprehensions (listomfattningar i boken)
def kasta_tärningar2(antal):
    return [randint(1,6) for _ in range(antal)]

# Uppgift 14
def medelvärde(lista):
    sum = 0
    n = 0
    for tal in lista:
        sum += tal
        n += 1
    return sum / n

# eller enklare
def medelvärde2(lista):
    return sum(lista) / len(lista)

# Uppgift 15

def faktorial(n):
    produkt = 1
    for i in range(n):
        n *= i
    return produkt

# eller (ÖVERKURS) med rekursion(!!?)
def faktorial2(n):
    if n==1:
        return 1
    else:
        return n*faktorial2(n-1)

# Uppgift 16
def är_primtal(tal):
    for x in range(2, int(tal**2)+1):
        if tal%x==0:
            return False
    return True

# Uppgift 17
def analysera_sträng(text):
    antal_tecken = len(text)
    antal_vokaler = 0
    antal_ord = 1
    vokaler = "aeiuoyåäö"
    text = text.lower().strip()
    # Anta att ord avgränsas med endast
    # ett mellanslag
    for tecken in text:
        if tecken in vokaler:
            antal_vokaler += 1
        if tecken==" ":
            antal_ord += 1
    return (antal_tecken, antal_ord, antal_vokaler)

print(analysera_sträng("Micke är bäst"))

# Uppgift 18
def filtrera_jämna(lista):
    jämna = []
    for tal in lista:
        if tal%2==0:
            jämna.append(tal)
    return jämna

#eller
def filtrera_jämna2(lista):
    return [x for x in lista if x%2==0]




