#Задание 1
x = int(input("Введите ваш возраст: "))
if x < 18:
    print("Вы несовершеннолетний")
elif 18 <= x <= 65:
    print("Вы трудоспособный")
else:
    print("Вы пенсионер")
#Задание 2
cost = int(input("Введите стоимость покупки: "))
if cost < 1000:
    print("Скидка не предоставляется")
elif 1000 <= cost <= 5000:
    print("Скидка 5%")
else:
    print("Скидка 10%")
#Задание 3
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
operation = input("Введите операцию (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Ошибка: деление на ноль!")
        exit()
else:
    print("Неверная операция.")
    exit()

print("Результат:", result)
#Задание 4
num0 = int(input("Введите число: "))

if num0 % 2 == 0 and (str(num0).endswith('2') or str(num0).endswith('6')):
    print("True")
else:
    print("False")
#Задание 5
password = 228
n = int(input("Введите пароль: "))
if n == password:
    print("Доступ разрешён")
else:
    print("Неверный пароль")
#Задание 6
a = input("Введите коорднаты квадрата: ")

if a == "b1" or a == "c1" or a == "c5" or a == "c9" or a == "c6" or a == "b3" or a == "b7" or a == "c4" or a == "c8":
    print("В данном квадрате обитает синий попугай")
elif a == "b2" or a == "b6" or a == "c2" or a == "c10" or a == "c7" or a == "c11" or a == "b4" or a == "b8":
    print("В данном квадрате обитает зелёный попугай")
else:
    print("Квадрат пустой")
#Задание 7
n = int(input("Введите первое число: "))
k = int(input("Введите второе число: "))
if n % k == 0:
    print("Все гуд")
else:
    print("Все не гуд")
#Задание 8
lvl = int(input("Введите ваш уровень: "))
hp = int(input("Введите ваше здоровье: "))

if lvl < 5:
    print("Ваш уровень слишком низкий для выполнения миссии.")
elif lvl > 5:
    if hp > 50:
        print("Вы готовы к миссии!")
    elif 20 <= hp <= 50:
        print("Ваше здоровье низкое будьте осторожны.")
    elif hp < 20:
        print("Ваше здоровье слишком низкое для выполнения миссии.")
    else:
        print("Некорректные данные.")
#Задание 9
inventory = ["яблоко", "шариковая ручка"]
missing_items = []
if "ключ" not in inventory:
    missing_items.append("ключ")
elif "фонарь" not in inventory:
    missing_items.append("фонарь")
elif len(missing_items) > 0:
    print("Не хватает предметов для прохождения: "+", " .join(missing_items))
else:
    print("Проходите")


    
