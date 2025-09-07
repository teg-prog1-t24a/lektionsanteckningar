# Vi gick igenom grunderna på tavlan
# Läs om dem i boken

# Här är ett exempel på hur vi kan använda
# index-operatorn [] för att gå igenom alla
# bokstäver i en sträng (och räkna antalet f)
s = "finished files are the result of years of scientific study combined with the experience of years"
print(s)
antal_f = 0
# Vi använder funktionen len för att avgöra hur lång vår sträng är
# och därmed hur lång vår loop skall vara
for i in range(0,len(s)):
    # Om tecken nr i är ett 'f' så räknar vi upp antalet
    if s[i]=='f':
        antal_f += 1
print(antal_f)
