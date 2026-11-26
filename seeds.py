# seeds.py: los "seeders". Dejan la base lista con datos básicos.
# Se EJECUTA (python seeds.py); no lo importa nadie.
# Siempre parte de cero: borra datos.db, crea las tablas y vuelve a insertar.
import database

if database.RUTA_DB.exists():
    database.RUTA_DB.unlink()
database.crear_tablas()

# 1: Tabla Padre: lugar
database.ejecutar_muchos(
    "INSERT INTO lugar (sala, comuna) VALUES (?,?)",
    [
    ("Teatro del Lircay", "Talca"),
    ("Sala Abate Molina", "Talca"),
    ("Teatro Provincial de Curicó", "Curicó"),
    ("Centro Cultural de Curicó", "Curicó"),   
    ]
)

# 2: AQUI VA LA TABLA NUMERO 2- 'valor'

print("Base creada con datos básicos.")
