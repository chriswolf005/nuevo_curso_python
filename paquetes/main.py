#Importar funciones de modulos dentro del paquete
from ecomerce.inventory import add_product, remove_product
from ecomerce.sales import process_sales

#Agregar un producto al inventario
add_product('Camisa', 10)
#Eliminar un producto del inventario
remove_product('Camisa')
#Procesar ventas
process_sales('Camisa', 3)
