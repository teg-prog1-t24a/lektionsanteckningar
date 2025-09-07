# Det här programmet användes för att demonstrera
# felsökning med hjälp av brytpunkter.

# Det är meningen att programmet skall summera
# kvadraterna. I loopen bör stå summa = summa + kvadrat
# istället för summa = kvadrat + x.
# Kanske enkelt att se men ibland stirrar man 
# sig blind även på enkla fel.

# Med hjälp av brytpunkter (breakpoints) som vi skapar
# som små röda cirklar genom att klicka till vänster om radnumret
# så kan vi pausa programmet, titta vad alla variabler har för värden,
# och gå framåt steg för steg för att se vad som händer

summa = 0
for x in range(10):
    kvadrat = x*x
    print(kvadrat)
    summa = kvadrat + x
print(summa)