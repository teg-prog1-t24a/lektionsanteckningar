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

