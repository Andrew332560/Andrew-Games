fruit_stock = {"apple": 42, "orange": 21, "banana": 12}

import tkinter

# Crea una ventana
window = tkinter.Tk()

# Establece el título de la ventana
window.title("Andres Games v1.1.1")

# Establece el tamaño de la ventana
window.geometry("500x300")

# Agrega un etiqueta a la ventana
label = tkinter.Label(window, text="🎮 Добро пожаловать в Андрес Игры! 🎮")
label.pack()

# Muestra la ventana
window.mainloop()

import os
os.system("title Андрес Игры v1.1.1")

import time

print("загрузка..")
time.sleep(3)

print('')
from os import system
system("cls")
print('Сначала создайте свою учетную запись и войдите в систему')
n1 = input('Имя ')
n2 = input('Пароль ')

system("cls")
print('Добро пожаловать в бета-версию Andres Games v1.1.1!')
print('ваша версия Andres Games Pre-Beta1.1.1')
print('')
print('----------------------------------------------')
print('                   Магазин                    ')
print('----------------------------------------------')
system("dir store")
print('')
print('----------------------------------------------')
print('                  библиотека                  ')
print('----------------------------------------------')
system("dir games")
print('')
print('Инструменты разработки Python')
print('Создано Андрес Групп')
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
