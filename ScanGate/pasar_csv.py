import csv
import sqlite3
import chardet

# Conexión a la base de datos SQLite
conexion = sqlite3.connect("db.sqlite3")
cursor = conexion.cursor()

# Detectar la codificación del CSV
with open("csvdatos.csv", "rb") as f:
    rawdata = f.read()
    result = chardet.detect(rawdata)
    encoding = result.get("encoding")

# Si la codificación no se detecta, usar una codificación predeterminada
if not encoding:
    encoding = "utf-8"

# Abrir el archivo CSV con la codificación detectada
archivo_csv = open("csvdatos.csv", "r", encoding=encoding)
lector_csv = csv.reader(archivo_csv)


# Omitir la primera fila (encabezado)
next(lector_csv)

# Insertar datos en la tabla
for fila in lector_csv:
    cursor.execute("""
INSERT INTO access_registros (
    nombre,
    hora_entrada,
    foto,
    ciudad_estado,
    correo,
    empresa,
    num_telefono,
    codigo_barras
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", fila)

# Guardar los cambios y cerrar la conexión
conexion.commit()
archivo_csv.close()
conexion.close()

print("¡Datos importados a la base de datos SQLite con éxito!")
