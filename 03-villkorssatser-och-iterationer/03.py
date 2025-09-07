# Det finns mycket inbyggd funktionalitet i Python
# Vi skall senare prata om detaljerna men man kan importera
# olika moduler i början av ett program för att kunna använda
# sådana funktioner 

# I modulen random finns funktioner för slumptal
# För stunden lär vi oss att använda dem utan att riktigt förstå
# eftersom det kan vara roligare att skriva exempel med lite slump i
import random

# Vi ska använda funktionen randint
# (kort för "random integer" eller slumpmässigt heltal)
# Vi använder den genom att skriva t ex random.randint(1,6)
# där 1 är lägsta värdet och 6 är högsta värdet vi kan få

# Den här koden simulerar och skriver ut resultatet 10 tärningsslag
for i in range(10):
    answer = random.randint(1,6)
    print(answer)

