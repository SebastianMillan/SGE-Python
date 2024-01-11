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