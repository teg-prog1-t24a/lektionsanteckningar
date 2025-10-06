lst = [0, 1, 2, 3, 4, 5]

# Slices
print( lst[1:4] )  # [1, 2, 3
print( lst[:3] )
print( lst[1:4:2] )
print( lst[::-1] )
print( lst[:-2] )


text = "hej"
lst = [x for x in text]
lst = list(text)
print(lst) # ["h", "e", "j"]

info = ("Micke", "Visby", 1975)
lst = list(info)

mening = "Jag är        bäst   "
lst = mening.split()
print(lst) # ["Jag", "är", "bäst"]

mening = "alfa,beta,gamma"
lst = mening.split(",")


lst = ["äpplen", "päron", "banan"]
text = ", hej hej, ".join(lst)
print(text)

lst = [1, 2, 3, 4, 5]
print( ", ".join(str(x) for x in lst) )