import csv
import os
home_dir=os.path.expanduser("~")#Ir a home
dowloads_dir=os.path.join(home_dir,'Downloads')#con esta linea entramos a descargas o la carpeta de preferencia
file_name="products.csv"#Este es el nombre del archivo
file_path=os.path.join(dowloads_dir,file_name)#Aqui construimos la ruta

new_product={
    'name':'Wireless charger',
    'price':20,
    'quantity':100,
    'brand':'samsung',
    'category':'Acessories',
    'entry':'2024-07-01'
}

with open(file_path,mode='a',newline='') as file:
    file.write('\n')
    csv_writer=csv.DictWriter(file,fieldnames=new_product.keys())
    csv_writer.writerow(new_product)