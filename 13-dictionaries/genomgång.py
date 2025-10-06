














# Mer om listor

# Repetition av slices

# För enkelhets skull väljer vi en lista med samma värden som sina index
lista = [0, 1, 2, 3, 4, 5, 6]

print(lista[0:3])   # Värdet på index 3 kommer INTE med
print(list[:3])     # Anger vi inget index så väljer Python första eller sista
print(list[1:6:2])  # En tredje parameter bestämmer steglängden
print(list[::-1])   # Negativa värden räknar bakifrån

# Omvandling till listor

# Strängar
text = "hej" 
lst = list(text)
print(lst)

# Tuples
info = ("Micke", "Visby", 1975)
lst = list(info)
print(lst)

# Meningar (eller text som är systematiskt avgränsad)
mening = "Jag är bäst"
lst = mening.split()
print(lst)

mening = "alfa,beta,gamma"
lst = mening.split(",")
print(lst)

# Från lista till sträng
lst = ["äpplen", "päron", "banan"]
text = ", ".join(lst) # Känns bakvänt, men så är det
print(text) 

lst = ["M", "i", "c", "k", "e"]
text = "".join(lst)
print(text)

# Fungerar bara med strängar
# Vad kan vi göra?
lst = [1, 2, 3, 4, 5]
lststr = [str(x) for x in lst]
text = ", ".join(lststr)
print(text)

# Enumerate
lst = ["Alfa", "Beta", "Gamma", "Delta"]
for idx, val in enumerate(lst):
    print(f"På plats {idx} har bokstaven {val}]")


###
### Dictionaries
###

# Ordbok eller lexikon ungefär
# Sök på ett ord och hitta ett värde
# Måste inte vara ord - men det är idén
# Vi använde NYCKLAR istället för index

ordbok = {
    "äpple": "apple",
    "apelsin": "orange",
    "gurka": "cucumber",
    "ananas": "pineapple"
} 

print(ordbok["äpple"])

for key in ordbok:
    print(key)

for key in ordbok:
    print(f"{key} har värdet {ordbok[key]}")

for key, val in ordbok.items():
    print(f"{key} har värdet {val}")

# Ta bort ett element ur en dictionary
del(ordbok["apelsin"])

# .keys() .values() .items()

fråga = "Vilket ord vill du översätta (t ex gurka): "
svar = ordbok.get(text, "vet inte")
print(f"Vad heter {fråga} på engelska? {svar}")

