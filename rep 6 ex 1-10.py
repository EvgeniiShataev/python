#Задание №1
names = ["Richard", "Igor", "Jonathan", "Alice", "Mary", "Bonnie"]
for i in names:
    print("Hello", i,"!")
#Задание №2
phrase = "I'm learning cycles."
for i in range(10):
    print(phrase)
#Задание №3
stations = ["Малиновка", "Рябиновка", "Суслово", "Дрожжино", "Звягино"]
for i in range(5):
    station = stations[i]
    if i == 4:
       print(f"Поезд на станции: {station} Конечная!")
    else:
        print(f"Поезд на станции: {station}.")   
#Задание 4
shop = ["Laptop", "Smartphone", "Watch", "Tablet", "Headphones"]
for x in shop:
    if x == "Laptop":
        print("Im buing this")
    else:
        print("I dont need it")
#Задание 5
tasks = ["Сдать проект (Важная)", "Сходить в магазин", "Позвонить врачу (Важная)", "Убраться в комнате", "Подготовить отчёт"]
for i,x in enumerate(tasks,start = 1):
    if "Важная" in x:
        print(f"{i}!: {x}")
    else:
        print(f"{i}: {x}")
#Задание 6
q = int(input("Введите кол-во чисел: "))
summ = 0
for i in range(q):
    w = int(input(f"Введите сами числа: "))
    summ += w
print("Сумма всех чисел:", summ)
#Задание 7
z = 0
while z < 10:
    z += 1
    print(f"цикл сработал {z} раз")
#Задание 8
while True:
    j = input("Введите команду для выбора направления движения: ")
    if j == "w":
        print("персонаж идёт вперёд")
    elif j == "a":
        print("персонаж идёт влево")
    elif j == "s":
        print("персонаж идёт назад")
    elif j == "d":
        print("персонаж идёт вправо")
    elif j == "stop":
        print("Программа остановлена")
        break
    else:
        print("Неизвестная команда! Попробуйте снова.")
#Задание 9
while True:
    num = int(input("Введите число от 1 до 9: "))
    if num < 1 or num > 9:
        print("Число вне диапазона. Попробуйте снова.")
    else:
        break
e = 1
while e <= 10:
    c = num * e
    print(f"{num} x {e} = {c}")
    e += 1
#Задание 10
s = "аганим"  
a = 3  
print("Вопрос от Жака Фреско: Что собирать первым слотом на лиона 4 поз?")
while a > 0:
    f = input("Ответ: ") 
    if f == s:  
        print("Хорош!")
        break 
    else:
        a -= 1  
        if a > 0:
            print(f"Неа! У тебя осталось {a} попыток.")
        else:
            print("Иди учись, узник лоу птс")
#делал в час ночи :(



    

    
