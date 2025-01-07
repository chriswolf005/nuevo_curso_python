from collections import deque

def manage_delivery_queue()-> deque:
    #Crea una cola para gestionar entregas de productos
    delivery_deque=deque(["order_1","order_2","order_3"])
    delivery_deque.append("Order_4")#Agregar al funal
    delivery_deque.appendleft("Order_0")#Agregar al principio
    delivery_deque.pop()
    delivery_deque.popleft()
    return delivery_deque

que=manage_delivery_queue()
print(que)