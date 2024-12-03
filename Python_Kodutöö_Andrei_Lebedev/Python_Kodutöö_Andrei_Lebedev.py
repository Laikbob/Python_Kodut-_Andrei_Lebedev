from ast import Try
import math

print("Ruudu karakteristikud")
while True:
    try:
        a=int(input("Sisesta ruudu külje pikkus => "))
        break
    except ValueError:
        print("Viga: sisestage arvväärtus.")
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt", P)
di=a*math.sqrt(2)
print("Ruudu diagonaal:", round(di,2))
print()
print("Ristküliku karakteristikud")
while True:
    try:
        b=int(input("Sisesta ristküliku 1. külje pikkus => "))
        break
    except ValueError:
        print("Viga: sisestage arvväärtus.")
while True:
    try:
        c=int(input("Sisesta ristküliku 2. külje pikkus => "))
        break
    except ValueError:
        print("Viga: sisestage arvväärtus.")
S=b*c
print("Ristküliku pindala", S)
P=2*(b+c)
print("Ristküliku ümbermõõt", P)
di=math.sqrt(b**2+c**2)
print("Ristküliku diagonaal", round(di,2))
print()
print("Ringi karakteristikud")
while True:
    try:
        r=int(input("Sisesta ringi raadiusi pikkus => "))
        break
    except ValueError:
        print("Viga: sisestage arvväärtus.")
d=2*r
print("Ringi läbimõõt" , (d))
S=math.pi*r**2
print("Ringi pindala", round(S,2))
C=2*math.pi*r
print("Ringjoone pikkus", round(C,2))
