import json

new_product={
    "name": "Bluetooth Speaker",
    "price": 80,
    "quantity": 50,
    "brand": "SoundWave",
    "category": "Audio",
    "entry_date": "2024-08-20",
    "expiry_date": "2026-08-20",
    "warehouse_location": "N14"
}

file_path='products.json'

with open(file_path,mode='r') as file:
    products = json.load(file)

products.append(new_product)

with open(file_path,mode='w') as file:
    json.dump(products,file,indent=4)