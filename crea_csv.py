import csv
import os

# Datos de ventas mensuales
ventas_mensuales = [
    {"mes": "Enero", "monto_vendido": 12000},
    {"mes": "Febrero", "monto_vendido": 15000},
    {"mes": "Marzo", "monto_vendido": 18000},
    {"mes": "Abril", "monto_vendido": 16000},
    {"mes": "Mayo", "monto_vendido": 17000},
    {"mes": "Junio", "monto_vendido": 14000},
    {"mes": "Julio", "monto_vendido": 13000},
    {"mes": "Agosto", "monto_vendido": 16000},
    {"mes": "Septiembre", "monto_vendido": 20000},
    {"mes": "Octubre", "monto_vendido": 21000},
    {"mes": "Noviembre", "monto_vendido": 22000},
    {"mes": "Diciembre", "monto_vendido": 25000},
]

# Obtener el directorio de Descargas del usuario
home_dir = os.path.expanduser("~")
downloads_dir = os.path.join(home_dir, 'Downloads')

# Nombre del archivo CSV
file_name = "ventas_mensuales.csv"
file_path = os.path.join(downloads_dir, file_name)

# Escribir los datos en el archivo CSV
with open(file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["mes", "monto_vendido"])
    writer.writeheader()
    for venta in ventas_mensuales:
        writer.writerow(venta)

print("Archivo CSV creado:", file_path)
