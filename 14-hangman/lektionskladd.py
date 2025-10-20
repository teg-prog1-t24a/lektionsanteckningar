
'''
Pseudokod är ett sätt att beskriva det viktiga
i t ex en algoritm eller ett program med hjälp
av nästan vanligt språk.

Låt x = 2
Så länge x mindre än 10
    Addera x till en summa
Skriv ut summan
'''

'''
Vi kan använda ungefär samma sätt att tänka
för att planera ett program innan vi börjar
att skriva den faktiska koden.

Nedan har vi byggt upp olika funktioner
som är vagt beskrivna men som hjälper oss
att strukturera upp koden innan vi ger oss
in på detaljerna i själva programmeringen.

Visa det delvis dolda ordet:
----------------------------
Skapa ett nytt tomt ord
För varje bokstav i det riktiga ordet
    Finns bokstaven bland gissade bokstäverna?
        Lägg till bokstaven i det nya ordet
    Annars
        Lägg till understreck (_) i det nya ordet

Spela en runda:
---------------
Välj ett korrekt ord
Så länge inte spelaren har vunnit eller förlorat
    Visa delvis dolda ordet
    Fråga efter gissning
    Kontrollera gissningen, eventuellt avsluta
    Rita galgen

Spela hela spelet:
------------------
Så länge spelet forsätter
    Spela en runda
    Fråga om spelaren vill spela igen
'''

# Del 2:
# Moduler och slumptal

# Vi kan importera kod från andra MODULER
# I Python ingår ett antal standardmoduler, t ex
# random och math

# Om vi använder from ... import ...
# kan vi välja exakt vilka funktioner vi vill kunna använda
# och då behöver vi inte skriva modulnamnet före
from random import randint, random

# Om vi bara använder import så kan vi använda
# vilka funktioner vi vill, men vi måste lägga till
# random. när vi använder dem, t ex random.randint(1,6)
import random
import math

# Om vi har flera egna filer i samma mapp så kan vi importera
# dem från varandra. Det är användbart t ex om vi skapar funktioner
# som vi vill använda från flera program (eller flera filer)
import mickes
print(mickes.throw_die())

# Random innehåller flera användbara funktioner, t ex
print(random.random()*200 - 100) # random.random() ger flyttal mellan 0 och 1
print(randint(1,6)) # heltal mellan a och b
random.choice(WORDS) # Väljer ett element ur en lista
random.shuffle(WORDS) # Blandar alla element i en lista i slumpmässig ordning
random.sample(WORDS, 2) # Väljer ett antal ord ur en lista

# Med print kan vi se vilka funktioner mm en modul innehåller (men bäst är oftast att läsa dokumentationen)
print(dir(math))
print(dir(random))

# Här nedanför är ett embryo till att göra ett hängagubbespel enligt planen längre upp i filen.
WORDS = ["citronsyracykeln", "integral", "höstlov"]
ALLOWED_CHARACTERS = "abcdefghijklmnopqrstuvwxyzåäö"

def play_round():
    idx = random.randint(0,len(WORDS)-1)
    word = WORDS[idx]
    while True:
        break


def main():
    is_playing = True
    while is_playing:
        play_round()
        inp = input("Vill du fortsätta? ")
        if inp=="nej":
            is_playing = False


main()
