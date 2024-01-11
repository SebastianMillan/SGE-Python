n=int(input('Indica un número'))

if n>1:
    print(True)
else:
    print(False)

a=5
b=10
if a==5:
    print('a vale', a)
    if b==10:
        print('y b vale', b)

if a==5 and b == 10:
    print("a vale 5 y b vale 10")
else:
    print("ni a vle 5 ni b vale 10")

nota = float(input("Introduce una nota: "))

if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 6:
    print("Bien")
elif nota >= 5:
    print("Suficiente")
else:
    print("Insuficiente")
