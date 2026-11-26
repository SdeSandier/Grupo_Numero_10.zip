# schemas.py: un modelo Pydantic por cada cosa que el cliente envía.
# Si el cuerpo no cumple, FastAPI responde 422 y tu función no se ejecuta.
from typing import Literal

from pydantic import BaseModel, Field

class LugarCrear(BaseModel):
    sala: str = Field(min_length = 1, max_length = 100)
    comuna: str = Field(min_length = 1, max_length = 100)

class LugarActualizar(BaseModel):
    # Solo se puede actualizar comuna, ya que 'sala' es la PK de la tabla, no se puede cambiar.
    comuna: str = Field(min_length = 1, max_length = 100)
