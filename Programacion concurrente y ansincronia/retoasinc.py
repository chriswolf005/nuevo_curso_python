"""
Implementar un sistema de descarga de archivos asincrónico 
donde cada archivo tarde un tiempo variable en descargarse.
"""
import asyncio
import random
async def download_file(file):
    print(f"Downloading {file}...")
    await asyncio.sleep(random.randint(1,10))
    print(f"Downloaded {file}")
    return file

async def main():
    print("Start")
    result=await download_file('archivo.txt')
    result2=await download_file('archivo2.txt')
    print(f"Result: {result}")
    print(f"Result: {result2}")

asyncio.run(main())