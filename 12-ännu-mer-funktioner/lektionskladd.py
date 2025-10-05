import random

# 1. Använd alltid main, inga variabler i globala scopet
# 2. Returnera flera värden
# 3. Default-värden på parametrar

# Med defaultvärden måste vi inte ange alla parametrar
# när vi anropar en funktion
def roll_dice(n = 5):
    '''Rulla n st tärningar (default 5)'''
    return [random.randint(1,6) for i in range(n)]

print(roll_dice())  # Slår fem tärningar
print(roll_dice(4)) # Slår fyra tärningar

# Det går att returnera flera värden i form av en tuple
def solve_quadratic(p, q):
    x1 = -p/2+((p/2)**2-q)**0.5
    x2 = -p/2-((p/2)**2-q)**0.5
    # Om det är entydigt behövs inte parenteser runt en tuple
    return x1, x2

# Vi kan spara tuplen eller packa upp den direkt om vi vill
result = solve_quadratic(7, 12)         # Spara tuplen i result
res1, res2 = solve_quadratic(11, 30)    # Packa upp i res1 och res2

# Med hjälp av try... except kan vi fånga fel
def input_float(text, felmeddelande = "Felaktig inmatning"):
    while True:
        # Vi försöker att köra koden efter try
        try:
            num = float(input(text))
            return num
        # Och om vi misslyckas hamnar vi här
        except ValueError:
            print(felmeddelande)

# Vi skall alltid använda en main-funktion i större program
# Det gör det lättare att göra rätt
def main():
    p1 = input_float("Ange p: ")
    q1 = input_float("Ange q: ")
    res1, res2 = solve_quadratic(p1, q1)
    print(f"Rötterna är {res1} och {res2}")

# Anropa main-funktionen längst ned i programmet
main()




