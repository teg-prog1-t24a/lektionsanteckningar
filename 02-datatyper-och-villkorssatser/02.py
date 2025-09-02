# Be användaren om indata
# Omvandla den på samma rad från sträng till flyttal
p = float(input("Mata in p: "))
q = float(input("Mata in q: "))

# Beräkna diskriminanten
diskriminant = (p/2)**2 - q
  
# Testa för de olika fallen
if diskriminant==0:
    # Dubbelrot
    print(f"x = {-p/2}")
elif diskriminant>0:
    x1 = -p/2+diskriminant**0.5
    x2 = -p/2-diskriminant**0.5
    print(f"x = {x1}")
    print(f"x = {x2}")
else:
    print("Reella lösningar saknas.")

