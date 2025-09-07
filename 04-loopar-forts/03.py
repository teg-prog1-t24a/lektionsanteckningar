# While-loopar är kraftfullare än for-loopar
# eftersom de inte behöver ha en förutbestämd längd
# från början. De använder ett villkor i början för
# att avgöra när de skall avbrytas

# En enkel while-loop kan fungera precis som en for-loop
tal = 0
while tal<10:
    print(tal)
    tal = tal + 1

# Men villkoret kan se ut precis hursomhelst.
# Jämför med if-satser.

# Vi kan också skapa oändliga loopar med hjälp av
# ett villkor som alltid är sant
# I så fall måste vi använda "break" för att hoppa
# ur loopen. I vissa fall ger det kod som är enklare att
# läsa.
while True: 
    tal = int(input("Välj ett tal mellan 1 och 10: "))
    if tal>=1 and tal<=10:
        break
print(f"Du valde talet {tal}.")
