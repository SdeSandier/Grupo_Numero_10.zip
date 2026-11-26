# main.py: crea la app y conecta los routers.
# Se ejecuta con:  python -m uvicorn main:app --reload
# Se ejecuta con:  py -m uvicorn main:app --reload 

from fastapi import FastAPI
from routers import lugar 

app = FastAPI(title="API Sonora Maule")


@app.get("/")
def inicio():
    return {"mensaje": "API de Sonora Maule funcionando"}


# Cada router trae los endpoints de una tabla. Aquí se conectan a la app.
app.include_router(lugar.router)
