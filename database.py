# database.py: el ÚNICO archivo que habla con SQLite.
# Lo usan seeds.py y todos los routers.
import sqlite3
from pathlib import Path

CARPETA = Path(__file__).parent          # la carpeta donde vive este archivo
RUTA_DB = CARPETA / "datos.db"
RUTA_SCHEMA = CARPETA / "schema.sql"


def conectar():
    con = sqlite3.connect(RUTA_DB)
    con.row_factory = sqlite3.Row        # las filas se leen por nombre de columna
    con.execute("PRAGMA foreign_keys = ON")   # SQLite lo pide en CADA conexión
    return con


def consultar(sql, params=()):
    """SELECT: devuelve una lista de diccionarios."""
    con = conectar()
    try:
        filas = con.execute(sql, params).fetchall()
        return [dict(f) for f in filas]
    finally:
        con.close()


def ejecutar(sql, params=()):
    """INSERT / UPDATE / DELETE: guarda el cambio y devuelve el id nuevo."""
    con = conectar()
    try:
        cur = con.execute(sql, params)
        con.commit()
        return cur.lastrowid
    finally:
        con.close()


def ejecutar_muchos(sql, lista_de_params):
    """Un mismo INSERT repetido para muchas filas (lo usan los seeders)."""
    con = conectar()
    try:
        con.executemany(sql, lista_de_params)
        con.commit()
    finally:
        con.close()


def crear_tablas():
    """Lee schema.sql y crea tablas, vista y triggers."""
    con = conectar()
    try:
        con.executescript(RUTA_SCHEMA.read_text(encoding="utf-8"))
    finally:
        con.close()
