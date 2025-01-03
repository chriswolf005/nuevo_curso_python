import csv
import os

home_dir = os.path.expanduser("~")  # Ir a home
downloads_dir = os.path.join(home_dir, 'Downloads')  # Entrar a la carpeta Descargas
file_name = "products.csv"  # Nombre del archivo
file_path = os.path.join(downloads_dir, file_name)  # Construir la ruta

updated_file_path = os.path.join(downloads_dir, 'products_updated.csv')
# Lista de empleados para asignar a las filas
employees = ['Juan', 'Maria', 'Pedro', 'Luis', 'Ana', 'Jose', 'Sara', 'Carlos', 'Diana', 'Miguel']
employee_count = len(employees)

with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    # Obtener los nombres de las columnas existentes
    fieldnames = csv_reader.fieldnames + ['total_value', 'empleado', 'supplier']
    rows = list(csv_reader)

    # Asignar diferentes empleados y un valor para 'supplier'
    for i, row in enumerate(rows):
        row['empleado'] = employees[i % employee_count]
        row['supplier'] = f'Supplier_{i % 5 + 1}'  # Agregar proveedores ficticios
        row['total_value'] = float(row['price']) * int(row['quantity'])

    with open(updated_file_path, mode='w', newline='') as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
        csv_writer.writeheader()  # Escribir encabezados

        for row in rows:
            csv_writer.writerow(row)
