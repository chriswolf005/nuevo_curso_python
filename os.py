import os

#Obtener el directorio actual
"""
cwd=os.getcwd()
print("Directorio de trabajo actual",cwd)
"""

#Listar los archivos .txt
"""
txt_files=[f for f in os.listdir('.') if f.endswith('txt')]
print("Los archivos txt son",txt_files)
"""

#Renombrar archivo
os.rename("hola.txt","holanuevo.txt")
print("Archivo renombrado")

#Listar los archivos .txt
txt_files=[f for f in os.listdir('.') if f.endswith('txt')]
print("Los archivos txt son",txt_files)