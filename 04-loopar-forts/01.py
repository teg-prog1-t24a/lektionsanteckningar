# Genom att placera loopar inuti varandra kan vi skapa
# alla kombinationer av flera variabler. Vi säger att vi
# nästlar (nest) dem, precis som med villkorssatser i olika nivåer.

# Vill vi skriva ut alla multiplikationstabeller
# upp till 10 kan vi använda två loopar
for tabell in range(1, 11):
    for faktor in range(1, 11):
        resultat = tabell*faktor
        print(f"{tabell}*{faktor}={resultat}")
    print()

# Vi kan om vi vill utnyttar den yttre loopvariabelns värde
# när vi skapar vår inre loop. Till exempel för att göra
# multiplikationstabeller som inte upprepar sig.

# För varje varv i den ytter (första) loopen så kommer
# den inre (andra) loopen att gå igenom alla sina tal
for tabell in range(1, 11):
    # Den inre loopen startar med det aktuella
    # värdet på loopvariabeln tabell och blir alltså
    # kortare för varje varv
    for i in range(tabell, 11):
        res = tabell*i
        print(f"{tabell}*{i}={res}")
    print()






