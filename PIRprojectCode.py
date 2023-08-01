import tkinter as tk
from tkinter import Tk
import matplotlib.pyplot as plt
from numpy import *


#Метод расчёта скорости фильтрации по введённым данным
def calculateSpeed(k, l, deltaP, miy):
    u = (k * deltaP) / (l * miy)
    return u

#Основной метод для произведения расчёта
def calculation():

    # Получение значений из блоков приложения
    Mn_i = float(Mn_il.get()) # начальное значение пористости (может быть любая)
    Y = float(Yl.get())  # значение кольматации
    an_i = float(an_il.get())  # начальное значение концентрации
    m_ct = float(m_ctl.get())  # значение статической пористости
    l = float(ll.get())  # половина длины трещины
    miy = float(miyl.get())  # значение вязкости
    deltaP = (int(P0l.get()) * 10**6) - (int(Pl.get()) * 10**6)  # значение перепада давления
    k = float(kl.get()) * 10**-13  # значение проницаемости
    time = int(timel.get()) # количество шагов
    countX = int(countXl.get())+1
    deltaX = l / countX  # количество координат 100, поэтому мы делим длину на эти 100 координат
    deltaT = 1  # шаг по времени

    # Создание массива и заполнение его начальным условиями
    Mn = [[0 for i in range(countX+1)] for j in range(2)]
    An = [[0 for i in range(countX+1)] for j in range(2)]
    for i in range(len(Mn[0])):
        Mn[0][i] = Mn_i
        Mn[1][i] = Mn_i
    An[0][0] = an_i
    An[1][0] = an_i

    #Высчитаем скорость фильтрации
    u = calculateSpeed(k, l, deltaP, miy) # значение скорости фильтрации
    print(u)

    # Начало расчёта концентрации и пористости
    for t in range(1, time):
        for i in range(0, countX):

                An[1][i+1] = An[0][i] - (Y * t * deltaT * An[0][i] * (Mn[0][i] - m_ct) * (1 - An[0][i]) / Mn[0][i]) - (
                            u * (An[0][i] - An[0][i - 1]) * deltaT * t / (deltaX*Mn[0][i]))
                print((u * (An[0][i] - An[0][i - 1]) * deltaT / (deltaX*Mn[0][i])))

                if Mn[0][i] - (Y * deltaT * (t) * An[0][i] * (Mn[0][i] - m_ct)) > m_ct:
                    Mn[1][i] = Mn[0][i] - (Y * deltaT * (t) * An[0][i] * (Mn[0][i] - m_ct))
                else:
                    Mn[1][i] = m_ct



        An[0] = An[1]
        Mn[0] = Mn[1]

    #Просчитываем последнюю координату, т.к. в цикле этот расчёт не производился

    #Выведение графиков на экран
    Mn[0][-1] = Mn[0][-2]
    Mn[1][-1] = Mn[1][-2]
    print(Mn)
    getGraph(An, Mn)

# Метод для выведения графика на экран
def getGraph(resA, resM):
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 2, 1)
    plt.plot(resA[-1][2:])
    plt.title("Концентрация")
    plt.xlabel('Координата x')
    plt.ylabel('Концентрация a')
    plt.subplot(2, 2, 2)
    plt.plot(resM[-1][2:])
    plt.title("Пористость")
    plt.xlabel('Координата x')
    plt.ylabel('Пористость M')
    plt.show()


# Метод для очистки панелей ввода с индекса '0' до конца
def clear():
    Mn_il.delete('0', 'end')
    Yl.delete('0', 'end')
    an_il.delete('0', 'end')
    m_ctl.delete('0', 'end')
    ll.delete('0', 'end')
    miyl.delete('0', 'end')
    P0l.delete('0', 'end')
    Pl.delete('0', 'end')
    kl.delete('0', 'end')
    timel.delete('0', 'end')
    countXl.delete('0', 'end')


# Создание окна для ввода данных
root = Tk(className='Python Examples - Window Color')
# root.geometry('700x350')
root.title('Программа для расчёта')
root["bg"] = "#DA7514"

# Добавление в окно текстовых блоков
tk.Label(root, text="Введите начальное значение пористости:", font=('Times', 14, 'bold'), bg="#DA7514", anchor='w').grid(row=0, sticky='w', padx=5, pady=5)
tk.Label(root, text="Введите значение кольматации:", font=('Times', 14, 'bold'), bg="#DA7514", anchor='w').grid(row=1, sticky='w', padx=5, pady=5)
tk.Label(root, text="Введите начальное значение концентрации:", font=('Times', 14, 'bold'), bg="#DA7514").grid(row=2, sticky='w', padx=5, pady=5)
tk.Label(root, text="Введите значение статической пористости:", font=('Times', 14, 'bold'), bg="#DA7514").grid(row=3, sticky='w', padx=5, pady=5)
tk.Label(root, text="Введите половину длины трещины:", font=('Times', 14, 'bold'), bg="#DA7514").grid(row=4, sticky='w', padx=5, pady=5)
tk.Label(root, text="Введите значение вязкости:", font=('Times', 14, 'bold'), bg="#DA7514").grid(row=5, sticky='w', padx=5, pady=5)
tk.Label(root, text="Введите начальное значение давления в Мегапаскалях:", font=('Times', 14, 'bold'), bg="#DA7514").grid(row=6, sticky='w', padx=5, pady=5)
tk.Label(root, text="Введите конечное значение давления в Мегапаскалях:", font=('Times', 14, 'bold'), bg="#DA7514").grid(row=7, sticky='w', padx=5, pady=5)
tk.Label(root, text="Введите значение проницаемости в Дарси:", font=('Times', 14, 'bold'), bg="#DA7514").grid(row=8, sticky='w', padx=5, pady=5)
tk.Label(root, text="Введите количество шагов по времени:", font=('Times', 14, 'bold'), bg="#DA7514").grid(row=9, sticky='w', padx=5, pady=5)
tk.Label(root, text="Введите количество координат:", font=('Times', 14, 'bold'), bg="#DA7514").grid(row=10, sticky='w', padx=5, pady=5)

# Добавление в окно полей ввода
Mn_il = tk.Entry(root)
Mn_il.insert(0, "0.2")
Mn_il.grid(row=0, column=1)

Yl = tk.Entry(root)
Yl.insert(0, "0.01")
Yl.grid(row=1, column=1)

an_il = tk.Entry(root)
an_il.insert(0, "0.3")
an_il.grid(row=2, column=1)

m_ctl = tk.Entry(root)
m_ctl.insert(0, "0.1")
m_ctl.grid(row=3, column=1)

ll = tk.Entry(root)
ll.insert(0, "100")
ll.grid(row=4, column=1)

miyl = tk.Entry(root)
miyl.insert(0, "0.001")
miyl.grid(row=5, column=1)

P0l = tk.Entry(root)
P0l.insert(0, "15")
P0l.grid(row=6, column=1)

Pl = tk.Entry(root)
Pl.insert(0, "10")
Pl.grid(row=7, column=1)

kl = tk.Entry(root)
kl.insert(0, "1")
kl.grid(row=8, column=1)

timel = tk.Entry(root)
timel.insert(0, "100")
timel.grid(row=9, column=1)

countXl = tk.Entry(root)
countXl.insert(0, "100")
countXl.grid(row=10, column=1)

# Клавиши вызывающие определённые методы при нажатии
#
# Произвести расчёт
tk.Button(root, text='Выполнить расчёт', command=calculation).grid(row=11, column=0, sticky='we', padx=120, pady=20)
# Очистить поля ввода
tk.Button(root, text='Очистить', command=clear).grid(row=11, column=1, sticky='we', padx=20, pady=20)

# Минимальный размер колонок
root.grid_columnconfigure(0, minsize=150)
root.grid_columnconfigure(1, minsize=150)
root.grid_rowconfigure(0)

# Выведение окна на экран
root.mainloop()