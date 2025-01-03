import os
home_dir=os.path.expanduser("~")#Ir a home
dowloads_dir=os.path.join(home_dir,'Downloads')#con esta linea entramos a descargas o la carpeta de preferencia
file_name="cuento.txt"#Este es el nombre del archivo
file_path=os.path.join(dowloads_dir,file_name)#Aqui construimos la ruta

with open(file_path, "r") as archivo:
    contador_lineas = 0
    for linea in archivo:
        contador_lineas += 1
print(f"El archivo tiene {contador_lineas} líneas.")
