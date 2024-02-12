from fastapi import FastAPI
from models.producto import Producto

app=FastAPI()

lista=[]
lista.append(Producto(id=1,nombre="camiseta",descripcion="descripcion camiseta",precio=12.5))
lista.append(Producto(id=2,nombre="champú",descripcion="descripcion champú",precio=8.2))
lista.append(Producto(id=3,nombre="reloj",descripcion="descripcion reloj",precio=50.0))

@app.get("/producto/")
async def get_all_producto():
    if len(lista)>0:
        return lista
    return "Lista vacia"

@app.get("/producto/{id}")
async def get_producto(id:int):
    return list(filter(lambda p: (p.id==id),lista))

@app.post("/producto/")
async def crear_producto(producto:Producto):
    return lista.append(producto)

@app.put("/producto/{id}")
async def editar_producto(id:int, producto:Producto):
    productoResult=list(filter(lambda p: (p.id==id),lista))
    indexResult=lista.index(productoResult[0])
    lista[indexResult]=producto

@app.delete("/producto/{id}")
async def delete_producto(id:int):
    list.remove(list(filter(lambda p: (p.id==id),lista)))
