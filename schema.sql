-- schema.sql: las tablas, la vista y los triggers de la bodega.
-- Lo lee database.crear_tablas(). En tu proyecto, aquí van los CREATE de tu Trabajo 3.
-- Regla: primero las tablas "padre" (las que no dependen de otras) y después las "hijas".

CREATE TABLE IF NOT EXISTS lugar (
    sala   TEXT NOT NULL UNIQUE PRIMARY KEY ,
    comuna TEXT NOT NULL
);

-- Tabla auxiliar: la BITÁCORA. La llenan los triggers; nadie la escribe a mano.
-- (No cuenta como una de tus 4 tablas: es el registro de lo que pasa en ellas.)
CREATE TABLE IF NOT EXISTS bitacora (
    id_bitacora INTEGER PRIMARY KEY,
    fecha_hora  TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
    tabla       TEXT NOT NULL,
    accion      TEXT NOT NULL,
    detalle     TEXT NOT NULL
);

--CREATE VIEW IF NOT EXISTS


--CREATE TRIGGER IF NOT EXISTS

