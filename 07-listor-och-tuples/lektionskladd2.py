lst = [17,6,3,223,8,533,1,63,354]
minsta_talet = None
for tal in lst:
    if minsta_talet is None or tal<minsta_talet:
        minsta_talet = tal
print(minsta_talet)
print(min(lst))


tup = ("Micke", 50)
print(tup)
print(tup[0])
namn = "Micke"

familjen = [
    ("Micke", 50), 
    ("Anna", 48), 
    ("Moa", 17), 
    ("Carl", 14)]
for namn, ålder in familjen:
    print(f"{namn} är {ålder} år")

namn, ålder = familjen[0]
familjen[0] = (namn, ålder+1)

a = 10
b = 8

temp = a
a = b
b = temp

a, b = b, a

x = 1
y = 3
coordinate = (x, y)

x, y = coordinate

# List comprehension
lst = []
for x in range(1,11):
    if x%2==0:
        lst.append(x*x)
print(lst)

lst = [x*x for x in range(1,11) if x%2==0]
print(lst)
