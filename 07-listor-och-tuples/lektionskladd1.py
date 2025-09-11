namn = "Micke"
ålder = 50
längd = 4/3

print(namn + " " + str(ålder) + " " + str(längd))
print(namn, ålder, längd)
print(f"Hej, jag heter {namn}! Jag är {ålder} år och {längd:.2f} m lång.")

text = "Micke"
for tecken in text:
    print(tecken)

åldrar = [50, 48, 17, 14]
for ålder in åldrar:
    print(ålder)

print(text[2])
print(åldrar[2]) 

åldrar[1] = 30
åldrar[0] += 1
åldrar[0] = åldrar[0] + 1
print(åldrar)

for ålder in åldrar:
    print(f"Ålder {ålder} år")

namnlista = ["Micke", "Anna", "Moa", "Carl"]
print(namnlista)

diverse = ["Micke", 51, 194.5]
parlista = [["Romeo", "Julia"], ["Adam", "Eva"], ["Jocke", "Jonna"]]

for par in parlista:
    print(f"{par[0]} älskar {par[1]}")

print(parlista[1][0])


print(åldrar[:])

åldrar_backup = åldrar
åldrar[0] += 1
print(åldrar)
print(åldrar_backup)


print(len(text))
print(len(åldrar))

print(åldrar.count(17))

åldrar.append(0)
namnlista.append("Sladdis")
print(namnlista)


minstingen = namnlista.pop(2)
print(f"{namnlista} får åka på semester, {minstingen} får stanna hemma")

lst = []
for i in range(3):
    tal = int(input("Mata in ett tal: "))
    lst.append(tal)

print(lst)
