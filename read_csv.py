import csv
import os
home_dir=os.path.expanduser("~")#Ir a home
dowloads_dir=os.path.join(home_dir,'Downloads')#con esta linea entramos a descargas o la carpeta de preferencia
file_name="products.csv"#Este es el nombre del archivo
file_path=os.path.join(dowloads_dir,file_name)#Aqui construimos la ruta


#Leer archivo
"""with open(file_path,mode='r') as file:
    csv_reader=csv.DictReader(file)
    for row in csv_reader:
        print(row)"""

#Mostrar la informacion por columnas
with open(file_path,mode='r') as file:
    csv_reader=csv.DictReader(file)
    for row in csv_reader:
        print(f"Producto:{row['name']},Precio:{row['price']}")