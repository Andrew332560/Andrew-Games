fruit_stock = {"apple": 42, "orange": 21, "banana": 12}

import tkinter

# Crea una ventana
window = tkinter.Tk()

# Establece el título de la ventana
window.title("Andres Games v1.1.1")

# Establece el tamaño de la ventana
window.geometry("500x300")

# Agrega un etiqueta a la ventana
label = tkinter.Label(window, text="🎮 Bienvenido A Andres Games! 🎮")
label.pack()

# Muestra la ventana
window.mainloop()

import os
os.system("title Andres Games v1.1.1")

import time

print("loading..")
time.sleep(3)

print('')
from os import system
system("cls")
print('Primero Crea tu Cuenta y inicia')
n1 = input('Nombre ')
n2 = input('Contraseña ')

system("cls")
print('Bievenidos A Andres Games Beta v1.1.1!')
print('tu Version de Andres Games Pre-Beta1.1.1')
print('web oficial https://andresdiazcraft.wixsite.com/andres-web')
print('')
print('----------------------------------------------')
print('                    Tienda                    ')
print('----------------------------------------------')
system("dir store")
print('')
print('----------------------------------------------')
print('                  biblioteca                  ')
print('----------------------------------------------')
system("dir games")
print('')
print('By Python Development Tools')
print('Creado Por el Grupo de Andres')
print('')
print('----------------------------------------------')
print('                     Cmd                      ')
print('----------------------------------------------')
print('')
system("cmd")
input()

import atexit

def prevent_exit():
    # Esta función se ejecutará indefinidamente
    # lo que evitará que el programa se cierre
    while True:
        pass

atexit.register(prevent_exit)

def main():
    # El programa se ejecutará indefinidamente
    # ya que la función `prevent_exit()`
    # se ejecutará indefinidamente
    pass

if __name__ == "__main__":
    main()
