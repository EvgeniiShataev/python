#Задание 1
m = ['круг', 0.25, 'квадрат', 'треугольник', 15, 'круг', 'овал', '10']
m.remove(0.25)
m.remove(15)
m.remove('10')
print(m)
#Задание 2
abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
del abc[1:5]
print(abc)
#Задание 3
numbers = [1, 4]
numbers.insert(1, 2)
numbers.insert(2, 3)
print(numbers)
#Задание 4
mass = [14, -6, 3, 11, 6, 8.5, 99, -20, -6, 10, 40, 0.25, -4, 5]
mass.pop(1)
mass.pop(6)
mass.pop(6)
mass.pop(-2)
mass.sort()
print(mass)
mass.sort(reverse=True)
print(mass)
#Задание 5 
pos = []
neg = []
zer = []
out1 = 0
out2 = 0
out3 = 0
num = int(input("Введите количество чисел: "))
for i in range(num):
    a = float(input("Введите число: "))
    if a > 0:
        pos.append(a)
    elif a < 0:
        neg.append(a)
    else:
        zer.append(a)
for i in neg:
    out1 += i
for i in pos:
    out2 += i
if len(pos) != 0:
    out2 = out2 / len(pos)
else:
    out2 = 0
out3 = list("*" * len(zer))
print(out1)
print(out2)
print(f"Количество звёзд: {len(zer)} {out3}")
