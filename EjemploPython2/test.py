print("Hola Mundo!")

saludo="Hola que pasa"
def saludar_a_todos():
    msg="Hola a todos"
    #global saludo -> Con esto la modificación de la variable se hace a nivel global, no solo del método
    saludo="saludo modificado solo dentro del metodo"
    print(msg)
    print("Dentro del metodo - "+saludo)

saludar_a_todos()
print("Fuera del metodo - "+saludo)
#print(msg) -> Se pierde esta variable porque se declara solo dentro del método

def saludar_v2():
    return saludo

print(saludar_v2())

def coord():
    return 34.2112,-32.3332

lat, ln = coord()
print(lat)
print(ln)

print(coord())

def suma(a,b):
    return a+b

print(suma(2,7))

def coord_v2(ciudad):
    if(ciudad=='Sevilla'):
        return 34.2112, -32.3332
    else:
        return 0,0

#Se puede reordenar la posición en la cuál introducimos los parametros en un metodo
def resta(a,b):
    return a-b;

print("Resta:",int(resta(b=6,a=2)))

def arg_indeterminados(*arg):
    print("Argumentos indeterminados:")
    for a in arg:
        print(a)

arg_indeterminados(1,2,2,3,"asdasd","hola",[1,2,"dd",True],False)