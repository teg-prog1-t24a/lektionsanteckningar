# Sammansatta datatyper
# Effektivt sätt att hantera mycket relaterad data

# En sträng är en rad av (ofta) relaterade tecken
# Vi såg att vi kunde iterera över dem i förra lektionen
text = "Micke"
for tecken in text:
    print(tecken)

# Vill vi göra samma sak för tal använder vi något som kallas listor
# Vi skapar en lista med hjälp av [ ] (samma som vi använder för index)
åldrar = [50, 48, 17, 14]

# Precis som för strängar kan vi plocka fram talet för ett speciellt index
print(åldrar[1])

# Precis som för strängar så börjar indexeringen på noll. [1] ger andra elementet.

# Till skillnad från strängar är en lista något som vi kan ändra i
# Vi kan ändra ett värde i listan genom att tilldela till ett index
åldrar[0] = 51
åldrar[3] += 1

# Python skriver ut en lista med hjälp av [ ] - syntaxen
print(åldrar)

# Men vi kan loopa igenom listan och skriva ut snyggare
# eller på andra sätt
for ålder in åldrar:
    # f-strängar var smidiga och kraftfulla vid bl a utskrift
    print(f"{ålder} år")

# En lista måste inte innehålla just tal
namnlista = ["Micke", "Anna", "Moa", "Carl"]
print(namnlista[0])

# ... eller ens samma datatyp (även om det är en bra
# grundregel att hålla sig till en typ per lista)
diverse = ["Micke", 51, 194.5]

# En lista kan till och med innehålla andra listor
par = [ ["Romeo", "Julia"], ["Adam", "Eva"], ["Jocke", "Jonna"] ]
print(par[2][0])

# Vi kan använda slices på våra listor
print(namnlista[:2])

# .. inklusive tricket för att vända på listan
print(namnlista)
print(namnlista[::-1])

# Om vi tilldelar listan till en annan variabel så är det SAMMA lista
# vi använder och förändrar
åldrar2 = åldrar
åldrar2[3] += 1
print(åldrar)

# Vill vi ha en kopia måste vi uttryckligen göra en
# Ett trick är att använda []-operatorn och göra en slice med alla element
åldrar3 = åldrar[:]

# Precis som för strängar finns en rad inbyggda metoder för listor

# Vissa heter samma sak
placeringar = [1, 2, 10, 3, 1, 4, 5]
print(placeringar.count(1))

# Några är användbara för att lägga till och ta bort
# element i listan (som vi inte kan göra för strängar)

# Lägg till i slutet på listan
namnlista.append("Sladdis")

# Se på egen hand .pop och .insert i boken

lst = []
for i in range(3):
    tal = int(input(f"Mata in tal {i}:"))
    lst.append(tal)
print(lst)

# Hitta minsta talet
# (Gör programmet här)

# Listor kan vi förändra, medan tuples är oföränderliga (immutable)
# och alltså fungerar som strängar
tup = ("Micke", 51)

# Vi kan inte använda t ex tup[1] += 1
namn, ålder = tup
tup = (namn, ålder+1)

# Bättre för värden som alltid hänger ihop i en viss ordning
# Vi använder () för att skapa tuplar (och ibland behövs inte ens parenteserna)
info = ("Micke", 51, 1.94)
print(info)

# Vi kan packa upp (unpack) en tuple i variabler
namn, ålder, längd = info
print(f"{namn} är {ålder} år gammal och {längd} m lång.")

# Hur kan vi växla värde mellan två variabler 
x = 5
y = 10

# Ett alternativ är att använda en temporär variabel
temporär = x
x = y
y = temporär

# Med tuples och uppackning kan vi skriva bytet kompakt
# och utan att införa en extra variabel
x, y = y, x

# Förklaringen till varför att det fungerar är att vi
# 1. på högersidan skapar en tuple med värdena från variablerna y, x
# 2. packar upp den och lägger resultatet i variablerna på vänstersidan (som står i omvänd ordning)


# List comprehensions (svårt men nyttigt)
# Förutom att lista elementen kan vi använda något som kallas list comprehensions
# Ett mellanting mellan loop och att skapa en lista
lst = [x for x in range(10)]

# Vi skulle kunna skriva som en vanlig loop med samma resultat
lst = []
for x in range(10):
    lst.append(x)

lst = [x*x for x in range(10)]

# Avancerade funktioner

# sorted ger kopia, .sort sorterar originalet
lista = [5, 4, 1, 2]
sorterad = sorted(lista)
print("Originallistan: ", lista)
print("Sorterad: ", sorterad)

lista.sort()
print("Originallistan: ", lista)
print("Sorterad: ", sorterad)

    

