import asyncio

async def process_data(data):
    print(f"Processing {data}...")
    #Simulamos un proceso de 10 segundo
    await asyncio.sleep(10)
    print(f"Data processed {data}")
    return data*2

async def main():
    print("Start")
    result=await process_data('archivo.txt')
    print(f"Result: {result}")

asyncio.run(main())