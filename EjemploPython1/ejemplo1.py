print("Hola mundo!")
nombre=input("Dime tu nombre")
print(type(nombre))
print(type(3/2))
print('Ejemplo de "comillas"')
print("""
Ejemplo
multilinea
""")
concatenar='concatenar'
print('Ejemplo de'+concatenar)

print(nombre[0]+nombre[1])
print(nombre[2:])
print(nombre[:2])
print(nombre[-4])

#nombre[1]='A' -> Da error, las cadenas son inmutables

print('Longitud: '+str(len(nombre)))
print(type(str(5)))

lista1=[1,2,3,4]
print(lista1)
print(type(lista1))

print(lista1[0])
print(lista1[2:])
print(lista1[:3])

lista2=["Hola", 2.22, None, -154]
print(lista2)
lista1[3]=88
concatenarLista=lista1+lista2
print(concatenarLista)
lista2[:2]=['asdasd','asdasda','asdasd']
print(lista2)

nombre = input('Indica tu nombre ->')
edad = input('Indica tu edad ->')
print(f"Me llamo {nombre} y tengo {edad} años")

x = 6
y = 2
z = 7

print(f"{x} mas {y} es igual a {x+y}")
print(f"{x} menos {y} es igual a {x-y}")
print(f"{x} por {y} es igual a {x*y}")
print(f"{x} dividido {y} es igual a {x/y}")

print(f"{z} dividido hacia abajo de {y} es igual a {z//y}")
print(f"El resto entre {z} y {y} es de {z%y}")
print(f"{x} elevado a {y} es igual a {x**y}")
print(f"La raíz cuadrada de {x} es de {round(x**0.5)}")

palabra = 'Hola Mundo'

print(palabra[0])
print(palabra[1])
print(palabra[-1])
print(palabra[0:4])