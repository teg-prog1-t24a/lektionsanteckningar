# Hela den här raden är en kommentar

födelseår = 2008  # Det här är också en kommentar

# Kommentarer står med fördel på en egen rad och ovanför
# den kod det avser, t ex

# Uppskatta vilken årskurs eleven går i
årskurs = 2010 - födelseår

# I VS code kan man snabbt göra ett helt stycke till
# kommentar genom att markera alla rader och sedan
# hålla ner Command och trycka först K och sen C
# (vilket förkortas ⌘ K ⌘ C).
# Avkommentare genom att markera och sedan ⌘ K ⌘ U.

# Det går också att kommentera med hjälp av strängar
'''
En sträng som står ensam på en rad blir en kommentar.
Praxis är då att använda tre citat-tecken (enkla
eller dubbla) så att det går att göra kommentarer på
flera rader.
'''

# Kommentarer med strängar används för att dokumentera
# funktioner. En sådan kommentar kallas docstring och skall
# bestå av en eller flera rader PRECIS under definitionen
# av funktionen.
def lös_andragradare(p, q):
    '''Löser en andragradare på pq-form.
    Returnerar en tuple med (x1, x2).'''
    return (0,0)

# En docstring syns när du håller muspekaren över
# funktionsnamnet, eller när du skriver första parentesen.
(x,y) = lös_andragradare(1,2)

# Du skall kommentera kodavsnitt som inte är 
# enkla att förstå för antingen
# - dig själv idag
# - dig själv i framtiden
# - en kompis/kollega

# Du bör inte skriva kommentarer som exakt berättar
# vad en rad kod gör ("sätt variabeln x till 5").
# Förklara hellre varför en kod gör något eller
# vad syftet med ett antal rader är.
