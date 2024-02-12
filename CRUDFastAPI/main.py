from typing import Annotated

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

from models.producto import Producto
from models.producto_dto import ProductoDTO
from models.user import User

app=FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

lista=[]
lista.append(Producto(id=1,nombre="camiseta",descripcion="descripcion camiseta",precio=12.5))
lista.append(Producto(id=2,nombre="champú",descripcion="descripcion champú",precio=8.2))
lista.append(Producto(id=3,nombre="reloj",descripcion="descripcion reloj",precio=50.0))

lista_user=[]
lista.append(User(id=1,username='sebas',password='1234', email='sebas@gmail', full_name='Sebastian Millan',disabled=False))
lista.append(User(id=2,username='fer',password='1234', email='fer@gmail', full_name='Fernando Claro',disabled=False))



@app.get("/producto/", status_code=200)
async def get_all_producto(token: Annotated[str, Depends(oauth2_scheme)]):
    if len(lista)>0:
        return lista
    return "Lista vacia"

@app.get("/producto/{id}",status_code=200)
async def get_producto(id:int, token: Annotated[str, Depends(oauth2_scheme)]):
    producto_encontrado=list(filter(lambda p: (p.id==id),lista))
    if len(producto_encontrado)==0:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto_encontrado[0]

@app.post("/producto/",status_code=201)
async def crear_producto(producto:ProductoDTO, token: Annotated[str, Depends(oauth2_scheme)]):
    nuevo_producto=Producto(id=len(lista)+1, nombre=producto.nombre, descripcion=producto.descripcion, precio=producto.precio)
    lista.append(nuevo_producto)
    return nuevo_producto

@app.put("/producto/{id}", status_code=200)
async def editar_producto(id:int, producto:ProductoDTO, token: Annotated[str, Depends(oauth2_scheme)]):
    producto_result=list(filter(lambda p: (p.id==id),lista))
    if len(producto_result)==0:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    index_result=lista.index(producto_result[0])
    lista[index_result]=Producto(id=id, nombre=producto.nombre, descripcion=producto.descripcion, precio=producto.precio)
    return lista[index_result]

@app.delete("/producto/{id}", status_code=200)
async def delete_producto(id:int,token: Annotated[str, Depends(oauth2_scheme)]):
    producto_borrado=list(filter(lambda p: (p.id==id),lista))
    if len(producto_borrado)==0:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return "Producto borrado con éxito"
