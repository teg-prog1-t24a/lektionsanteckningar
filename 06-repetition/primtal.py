# Det här programmet fungerar. Men hur?

inp = input("Vilket tal vill du kolla om det är ett primtal? ")
tal = int(inp)

# Vi börjar med att anta att talet är ett primtal
# Oskyldig till att vara delbar tills motsatsen är bevisad
är_primtal = True
delare = 2
while delare<tal:
    if tal % delare == 0:
        # Här hittade vi en delare
        # Vi har bevisat att det inte är ett primtal
        # Vi ändrar vårt påstående till falskt
        är_primtal = False
        # Vi behöver inte testa fler tal och kan avsluta
        # loopen i förtid
        break
    delare = delare + 1

# Om hela loopen gick klart så testade vi alla
# möjliga delare utan att hitta någon, vilket är
# kravet på ett primtal. Om vi alltså inte ändrade
# är_primtal till False i loopen så har det kvar
# värdet True

# Nu kan vi använda vårt värde för att skriva
# ut resultatet
if är_primtal:
    print("Primtal")
else:
    print("Ej primtal")

