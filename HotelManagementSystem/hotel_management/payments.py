# hotel_management/payments.py
import asyncio
import random


async def process_payment(customer_name: str, amount: float) -> bool:
    """Simula el procesamiento asíncrono de un pago."""
    print(f"Procesando pago de {customer_name} por ${amount}...")
    await asyncio.sleep(random.randint(1, 3))  # Simula el retardo en la operación de pago
    print(f"Pago de ${amount} completado para {customer_name}")
    return True
