tupla1=(1,2,3,"Hola",2.3)
tuplaAdd=(1,2)
tupla2=tupla1+tuplaAdd
print(tupla1)
print(tupla2)

t=(1,2,3)
lista=list(t)
lista.append(4)
t2=tuple(lista)
print(t2)

#Al añadir la lista en un set nos quita los repetidos
l=[1,1,1,1,2,2,2,3,2,3,3,2,2,2,2,2,2,5,5,4,4]
conjunto=set(l)
print(l)
print(conjunto)

frase="La parte contratante de la primera parte..."

s= set(frase)
print(frase)
print(s)