from fastapi import FastAPI

from models.producto import Producto

app=FastAPI()
lista=[]
@app.get("/producto/")
async def getAllProducts():
    if len(lista)>0:
        return lista
    return "Lista vacia"


@app.get("/producto/{id}")
async def getOneProduct(id:int):
    pass

@app.post("/producto/")
async def crearProducto(producto:Producto):
    pass

@app.put("/producto/{id}")
async def editarProducto(id:int, producto:Producto):
    pass

@app.delete("/producto/{id}")
async def deleteProducto(id:int):
    pass
