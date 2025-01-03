import os
home_dir=os.path.expanduser("~")#Ir a home
dowloads_dir=os.path.join(home_dir,'Downloads')#con esta linea entramos a descargas o la carpeta de preferencia
file_name="cuento.txt"#Este es el nombre del archivo
file_path=os.path.join(dowloads_dir,file_name)#Aqui construimos la ruta usando la variable donde tenemos la ruta de descarga + el nombre

try:

    with open(file_path,'r',encoding='utf-8') as file:
        for lineas in file:
            print(lineas.strip())

except FileNotFoundError:
    print(f"El archivo en la ruta {file_path} no fue encontrado.")
except Exception as e:
    print(f"Ocurrió un error al leer el archivo: {e}")


#Leer un archivo linea por linea
"""
with open(file_path,'r') as file:
    lines=file.readlines()
    print(lines)
"""
#Editar el texto
"""
with open(file_path,'a') as file: #Esto significa append agregar al final
    file.write("\n\nBy:no sabe tu")
"""

#Podemos usar "W" write pero eliminara todo lo que ya esta asi que cuidado

#Sobreescribir el texto

with open(file_path,'w') as file:
    file.write("\n\nBy:no sabe tu")