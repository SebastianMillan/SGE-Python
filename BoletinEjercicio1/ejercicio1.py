opcion = 1
palabrasDicc={}
contador=0

def cargar_palabras():
    palabras_file=open("palabras.txt").readlines()
    palabras_file_dicc={}
    for i in range(0, len(palabras_file)):
        palabras_file_dicc[palabras_file[i]]=0
        for palabraEnc in palabras_file:
            if(palabraEnc==palabras_file[i]):
                palabras_file_dicc[palabras_file[i]]+=1
    return palabras_file_dicc


while opcion != '0':
    print("""
        MENU
        1-Importar palabras clave
        2-Mostrar palabras clave
        0-Salir
    """)
    opcion=input('Indica que deseas hacer:')
    if opcion=='1':
        palabrasDicc=cargar_palabras()
    elif opcion=='2':
        for palabra in palabrasDicc:
            if (contador <= 19):
                print(palabra.replace("\n","")+"->"+str(palabrasDicc[palabra]))
                contador+=1
        for palabra in list(palabrasDicc):
            if(contador<=19):
                palabrasDicc.pop(palabra)
                contador+=1
        contador=0
    elif opcion=='0':
        print("Salir")
    else:
        print("Valor indicado erróneo")


print("Apagando el programa")




