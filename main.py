from tkinter import *
import shutil
import os
import time
import easygui
from tkinter import filedialog
from tkinter import messagebox as mb

import http.server
import socketserver

# PORT = 8000
#
# handler = http.server.SimpleHTTPRequestHandler
#
# with socketserver.TCPServer(("", PORT), handler) as httpd:
#     print("Server started at localhost:" + str(PORT))
#     httpd.serve_forever()




    # отрыть окно файла при выборе файла
def open_window():
    read = easygui.fileopenbox()
    return read

    # функция открытия файла
def open_file():
    string = open_window()
    try:
        os.startfile(string)
    except:
        mb.showinfo("Подтвердить", "Файл не найден!")

    # функция копирования файла
def copy_file():
    source1 = open_window()
    destination1 = filedialog.askdirectory()
    shutil.copy(source1, destination1)
    mb.showinfo("Подтвердить", "Файл скопирован!")

    # функция удаления файла
def delete_file():
    del_file = open_window()
    if os.path.exists(del_file):
        os.remove(del_file)
    else:
        mb.showinfo("Подтвердить", "Файл не найден!")

    # функция переименования
def rename_file():
    chosenFile = open_window()
    path1 = os.path.dirname(chosenFile)
    extension = os.path.splitext(chosenFile)[1]
    print("Введите новое имя для выбранного файла")
    newName = input()
    path = os.path.join(path1, newName + extension)
    print(path)
    os.rename(chosenFile, path)
    mb.showinfo("Подтверждение", "Файл переименован!")

    # функция перемещения файла
def move_file():
    source = open_window()
    destination = filedialog.askdirectory()
    if (source == destination):
        mb.showinfo("Подтверждение", "Источник и место назначения совпадают!")
    else:
        shutil.move(source, destination)
        mb.showinfo("Подтверждение", "Файл перемещен!")

    # функция создания новой папки
def make_folder():
    newFolderPath = filedialog.askdirectory()
    print("Введите имя новой папки")
    newFolder = input()
    path = os.path.join(newFolderPath, newFolder)
    os.mkdir(path)
    mb.showinfo("Подтверждение", "Папка создана!")

    # функция удаления папки
def remove_folder():
    delFolder = filedialog.askdirectory()
    os.rmdir(delFolder)
    mb.showinfo("Подтверждение", "Папка удалена!")

    # функция для вывода списка всех файлов в папке
def list_files():
    folderList = filedialog.askopenfile()
    sortlist = sorted(os.listdir(folderList))
    i = 0
    print("Файлы в", folderList, "папке:")
    while (i < len(sortlist)):
        print(sortlist[i] + '\n')
        i += 1

def info_file():
    path_file = filedialog.askopenfilename()
    checkfile = os.path.isfile(path_file)
    if checkfile:
        print("Файл")
        file = open(path_file, "r")
        read = file.read()
        file.close()
        print(read)
    else:
        print("Не файл")

    #функция даты файла
def date_file():
    date_file = filedialog.askopenfilename()
    date = os.path.getctime(date_file)
    print(time.ctime(date))

    # функция даты папки
def date_folder():
    date_folder = filedialog.askdirectory()
    date = os.path.getctime(date_folder)
    print(time.ctime(date))

    # функция сохранения данных в файле
def save_file():
    save_file = filedialog.askopenfilename()
    f = open(save_file, 'w')
    f.write(input())
    print('Готово')


window = Tk()
# # метка и кнопки для выполнения операций
Label(font=("Helvetica", 16), fg="blue").grid(row=5, column=2)
window.title("Добро пожаловать")
window.geometry('400x400')

Button(window, text="Дата папки", command=date_folder).grid(row=1, column=2)
Button(window, text="Дата файла", command=date_file).grid(row=5, column=2)
Button(window, text="Содержимое файла", command=info_file).grid(row=10, column=2)
Button(window, text="Открыть файл", command=open_file).grid(row=15, column=2)
Button(window, text="Скопировать файл", command=copy_file).grid(row=25, column=2)
Button(window, text="Удалить файл", command=delete_file).grid(row=35, column=2)
Button(window, text="Переименовать файл", command=rename_file).grid(row=45, column=2)
Button(window, text="Переместить файл", command=move_file).grid(row=55, column=2)
Button(window, text="Создать папку", command=make_folder).grid(row=75, column=2)
Button(window, text="Удалить папку", command=remove_folder).grid(row=65, column=2)
Button(window, text="Список всех файлов в каталоге", command=list_files).grid(row=75, column=2)
Button(window, text="Сохранить данные в файле", command=save_file).grid(row=85, column=2)

window.mainloop()
