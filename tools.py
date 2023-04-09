import os

def clear_screen():
    # Encapsulamos la lógica para borrar la pantalla en una función
    os.system('cls' if os.name == 'nt' else 'clear')
