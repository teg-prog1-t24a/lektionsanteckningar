# Med funktioner slipper vi skriva saker många gånger
print("Hello, World!")

# Kod som är definierad någon annanstans
# Vi behöver inte veta hur koden fungerar
# Med ett tydligt namn kan vi gissa vad som kommer att hända

x = int("75")
# inp = input("Vad heter du? ")

# Funktioner har samma "utseende" som i matte
# funktionsnamn ( argument )
namn = "Micke"
print("Hello", namn, end="")

# Funktioner kan ta argument
print("Detta argument är en sträng")
# Utan argument skrivs t ex en tom rad ut
print()

# Funktioner kan ge returvärden
# inp = input("Vad heter du? ")

# Om använder skriver Micke blir "Micke" returvärde
# som vi "stoppar in" i inp (tilldelar till variabelna inp)
print() # Ger inget returvärde
a = print() # a blir None

import random
# Ser vi till att flera funktioner blir tillgänliga från
# andra MODULER
slumptal = random.randint(1, 6)

from random import randint
slumptal = randint(1, 12)

# modul för matematik
from math import cos, sin, sqrt, pi
print(cos(2*pi/90))

# EGNA funktioner
# def funktionsnamn ( argument1 ) :
def skrik(text):
    print(text.upper() + "!")

skrik("Micke är bäst")
skrik("Ja, det är han")
# Välj funktionsnamn och namn på argument
# så att det är tydligt vad funktionen gör
# Man väljer OFTAST att låta funktioner
# vara verb

# Egna funktioner kan också ha returvärden
# vi använder return för att bestämma vad som
# skall returneras (dvs skickas tillbaka AV
# funktionen TILL den som anropade den)
def roll_die():
    return randint(1,6)

print(roll_die())
die = roll_die()
print(die)

def roll_dice(num):
    num = 5
    lst = []
    for i in range(num):
        lst.append(roll_die())
    return lst

player1 = roll_dice(5)
player2 = roll_dice(5)

num = 6
print(roll_dice(num))
print(num)
