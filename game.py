import random

# Bienvenida
print("*" * 80)
print("Bienvenido al game de fuego, agua o hojas, es similar a piedra, papel o tijeras")
print("*" * 80)

# Contadores de rondas ganadas
user_wins = 0
IA_wins = 0

# Definir las opciones posibles
opciones = ["fuego", "hojas", "agua"]

while user_wins < 3 and IA_wins < 3:
    # Elección de Usuario
    print("\nElije tu ataque-> 🔥💧🍃")
    user = input("Elige tu opción (fuego, hojas, agua): ").lower()

    # Validar la opción del usuario
    if user not in opciones:
        print("Opción no válida. Por favor elige fuego, hojas o agua.")
        continue

    # Opción aleatoria para la IA
    IA = random.choice(opciones)
    print(f"La IA ha elegido: {IA}")

    # Reglas del juego
    if user == "fuego" and IA == "fuego":
        print("Fuego y Fuego es un empate en llamas! 🔥")
    elif user == "fuego" and IA == "hojas":
        print("El fuego quema las hojas, ¡gana el User!")
        user_wins += 1
    elif user == "fuego" and IA == "agua":
        print("El agua apaga el fuego, ¡gana la IA!")
        IA_wins += 1
    elif user == "hojas" and IA == "fuego":
        print("El fuego quema las hojas, ¡gana la IA!")
        IA_wins += 1
    elif user == "hojas" and IA == "hojas":
        print("Hojas y Hojas es un empate verde! 🍃")
    elif user == "hojas" and IA == "agua":
        print("Las hojas absorben el agua, ¡gana el User!")
        user_wins += 1
    elif user == "agua" and IA == "fuego":
        print("El agua apaga el fuego, ¡gana el User!")
        user_wins += 1
    elif user == "agua" and IA == "hojas":
        print("Las hojas absorben el agua, ¡gana la IA!")
        IA_wins += 1
    elif user == "agua" and IA == "agua":
        print("Agua y Agua es un empate líquido! 💧")

    # Mostrar el marcador actual
    print(f"Marcador: User {user_wins} - IA {IA_wins}")

# Determinar el ganador final
if user_wins == 3:
    print("\n¡Felicidades! ¡El usuario ha ganado el juego! 🎉")
else:
    print("\n¡La IA ha ganado el juego! ¡Intenta de nuevo! 🤖")
