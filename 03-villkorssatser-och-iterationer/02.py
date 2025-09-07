# range ger ett intervall med heltal
# 0 1 2 3 4 5 6 7 8 9

# x är loopvariabel, dvs
# för varje varv i loopen får x ett nytt värde ur rangen
for x in range(1, 11):
    print(x)

# Om vi t ex vill summera alla tal i en range
# så skapar vi en variabel utanför loopen med ett
# lämpligt startvärde
summa = 0
for x in range(1, 1001):
    # Vi uppdaterar variabeln genom att
    # addera till den i varje varv och tilldela
    # svaret till samma variabel
    summa = summa + x
# Efter loopen kan vi skriva ut summan
print(summa)

