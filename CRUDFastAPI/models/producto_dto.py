from pydantic import BaseModel


class ProductoDTO(BaseModel):
    nombre:str
    descripcion:str | None=None
    precio:float

