inp = input("Vilket tal vill du kolla om det är ett primtal? ")
tal = int(inp)

är_primtal = True
delare = 2
while delare<tal:
    if tal % delare == 0:
        print(delare)
        är_primtal = False
    delare = delare + 1

if är_primtal:
    print("Primtal")
else:
    print("Ej primtal")

