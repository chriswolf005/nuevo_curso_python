from collections import Counter

def count_products(orders:list[str])->Counter:
    #Usa Counter para contar cuantos productos de cada tipo se han vendido
    return Counter(orders)


orders=['laptop','smartphone','lamp','car','laptop']

result=count_products(orders)
print(result)