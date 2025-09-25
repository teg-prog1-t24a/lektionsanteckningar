inp = input("Hur gammal är du? ")
age = int(inp)
print(f"Nästa gång du fyller år blir du {age} år")

# input, int och print är funktioner

# En funktion består av kod som är definierad
# någon annanstans. Genom att använda funktioner
# slipper vi uppfinna hjulet på nytt varje gång.

# Genom att ge funktioner tydliga namn så blir också
# vår kod mer lättläst. Vi behöver bara koncentera oss
# på att förstå vissa delar av koden i taget.

# Den kan vara skriven av någon annan, men vi kan
# också göra egna funktioner.

# Argument
print("Hej!")
print("Micke")
person1 = "Romeo"
person2 = "Julia"
print(person1, person2)

# Returvärden
text = "1975"
num = int(str)

import random
num = random.randint(1, 100)
print(num)

# Egna funktioner
def skrik(text):
    print(text.upper() + "!")

skrik("Hej Micke")

# Egna returvärden
def roll_die():
    return random.randint(1,6)

x = roll_die()
print(x)

print(roll_die())

# Funktioner i flera lager
def roll_dice(num):
    dice = []
    for r in range(num):
        dice.append(roll_die())

lst = roll_dice(5)
print(lst)

print(roll_dice(5))

# Standardfunktioner
import random

from random import randint

from math import sqrt, sin, cos


