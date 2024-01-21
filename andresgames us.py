fruit_stock = {"apple": 42, "orange": 21, "banana": 12}

import tkinter

# Crea una ventana
window = tkinter.Tk()

# Establece el título de la ventana
window.title("Andres Games v1.1.1")

# Establece el tamaño de la ventana
window.geometry("500x300")

# Agrega un etiqueta a la ventana
label = tkinter.Label(window, text="🎮 Welcome to Andres Games! 🎮")
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
print('First Create your Account and log in')
n1 = input('Username ')
n2 = input('Password ')

system("cls")
print('Welcome to Andres Games Beta v1.1.1!')
print('your Version of Andres Games Pre-Beta1.1.1')
print('')
print('----------------------------------------------')
print('                    Store                     ')
print('----------------------------------------------')
system("dir store")
print('')
print('----------------------------------------------')
print('                   library                    ')
print('----------------------------------------------')
system("dir games")
print('')
print('By Python Development Tools')
print('Created By Andres Group')
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
