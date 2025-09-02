# Be användaren om indata
# Omvandla den på samma rad från sträng till flyttal
p = float(input("Mata in p: "))
q = float(input("Mata in q: "))

# Beräkna lösningarna till andragradsekvationen
# x^2 + px + q = 0
x1 = -p/2 + ((p/2)**2 - q)**0.5
x2 = -p/2 - ((p/2)**2 - q)**0.5

# Skriv ut resultatet
# Konvertera talen x1, x2 till strängar
# för att kunna slå ihop dem med texten före
print("x1=" + str(x1))
print("x2=" + str(x2))

