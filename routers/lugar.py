import sqlite3
from fastapi import APIRouter, HTTPException, status
import database
from schemas import LugarActualizar, LugarCrear

router = APIRouter(prefix="/lugares", tags=["Lugares"])

@router.get("")
def listar_lugares():
    """Lista las salas existentes en la base de datos."""
    return database.consultar("SELECT sala, comuna FROM lugar ORDER BY sala ASC")

@router.get("/{sala}")
def obtener_lugar(sala:str):
    """Obtienen una sala al escribir su nombre."""
    filas = database.consultar(
        "SELECT sala, comuna FROM lugar WHERE sala = ?",
        (sala,),
    )
    if not filas:
        raise HTTPException(status_code = 404, detail = "No existe esa sala")
    return filas[0]

@router.post("", status_code = 201)
def crear_lugar(datos:LugarCrear):
    """Crea una nueva sala."""
    try:
        database.ejecutar(
            "INSERT INTO lugar (sala, comuna) VALUES (?, ?)",
            (datos.sala, datos.comuna),
        )
    except sqlite3.IntegrityError as error:
        raise HTTPException(status_code = 400, detail = f"No se pudo crear la sala: {error}",)
    return {"sala": datos.sala, "comuna": datos.comuna}

@router.put("/{sala}")
def actualizar_lugar(sala:str, datos: LugarActualizar):
    """Actualiza una comuna existente"""
    comuna_actualizar = database.consultar(
        "SELECT sala FROM lugar WHERE sala = ?",
        (sala,),
    )
    if not comuna_actualizar:
        raise HTTPException(status_code = 404, detail = "La sala no existe")
    
    try:
        database.ejecutar(
            "UPDATE lugar SET comuna = ? WHERE sala = ?",
            (datos.comuna, sala), 
        )
    except sqlite3.IntegrityError as error:
        raise HTTPException(status_code = 400, detail = f"No se pudo actualizar la sala: {error}",)
    return {"sala":sala, "comuna":datos.comuna}

@router.delete("/{sala}")
def eliminar_lugar(sala:str):
    """Elimina una sala si no tiene registros dependientes."""
    sala_eliminar = database.consultar(
        "SELECT sala FROM lugar WHERE sala = ?",
        (sala,),
    )
    if not sala_eliminar:
        raise HTTPException(status_code = 404, detail ="La sala no existe")
    try:
        database.ejecutar(
            "DELETE FROM lugar WHERE sala = ?", 
            (sala,),
        )
    except sqlite3.IntegrityError as error:
        raise HTTPException(status_code = 400, detail = f"No se pudo eliminar la sala (posible referencia activa en otra tabla): {error}")
    return {"mensaje": "Sala eliminada", "sala": sala}
