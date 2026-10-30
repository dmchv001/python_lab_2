print("Hello,world!")                                                            #задание 3
name = "Иван"                                                                    #задание 4
age = 19
height = 180
is_student = True
print("Значения:")
print("Имя:", name)
print("Возраст:", age)
print("Рост:", height)
print("является ли студентом?", is_student)
print("Типы переменных:")
print("Тип: name:", type(name))
print("Тип: age:", type(age))
print("Тип: heigt:", type(height))
print("Тип: student:", type(is_student))
name = "Артём"
age = 21
print("Изменение значений для задания 4:")
print("Изменённое имя:", name)
print("Изменённый возраст:", age)
first_name = input("Введите имя:")                                               #задание 5
last_name = input("Введите фамилию:")
age_base = input("Введите возраст:")
print("Тип возраста до преобразования:", type(age_base))
age = int(age_base)
height = float(input("Введите рост:"))
print("Пользователь:", first_name, " ", last_name, type(first_name), " ", type(last_name))
print("Возраст:", age, " ", type(age))
print("Рост:", height, type(height))
a = 15                                                                           #задание 6
b = 4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
print("Без скобок:", 2+3*4)
print("Со скобками:", (2+3)*4)
c = float(input("Введите любое число:"))                                         #задание 7
d = float(input("Введите ещё одно любое число:"))
print(c+d)
print(c-d)
print(c*d)
if d !=0:
    print(c/d)
else:
    print("Деление на ноль невозможно")
print("Цикл 1-10:")                                                              #задание 8
for i in range(1, 11):
    print(i, end = " ")
print()
print("Цикл 10-1:")
for i in range(10,0,-1):
    print(i, end = " ")
print()
print("Цикл чётных чисел:")
for i in range(0, 20, 2):
    print(i, end = " ")
print()
print("Цикл с изменённым шагом:")
for i in range(0, 20, 4):
    print(i, end = " ")
print()
z = int(input("Введите одно любое целое положительное число: "))                  #задание 9
if z <= 0:
    print("Введённые данные неверны: число должно быть целым и положительным")
elif z > 0:
    s = 0
print()
n = z
for i in range (1, n + 1):
    s += i
print("Сумма всех чисел цикла:", s)
count = 10                                                                        #задание 10
while count >= 1:
    print(count, end = " ")
    count -= 1
print()
import math                                                                       #задание 11
radius = float(input("Введите произвольное значение радиуса: "))
l = 2 * math.pi * radius
print("Длина окружности: ", l)
S = radius * radius * math.pi
print("Площадь круга: ", S)
z = int(input("Введите одно любое целое положительное число: "))                  #задание 12
if z <= 0:
    print("Введённые данные неверны: число должно быть целым и положительным")
if z > 0:
    print("Число положительное")
elif z < 0:
    print("Число отрицательное")
else:
    print("Число равно нулю")
y = z % 2
if y == 0:
    print("Число чётное")
else:
    print("Число нечётное")
age = int(input("Введите свой возраст: "))                                        #задание 13
has_access_input = input("Допуск имеется? (yes/no): ")
has_access = has_access_input.lower() == "yes"
if age >= 18 and has_access:
    print("Доступ разрешён")
else:
    print("Доступ запрещён")
n = int(input("Введите количество измерений: "))
if n <= 0:
    print("Ошибка: количество измерений должно быть больше 0")
else:
    summ = 0.0
for i in range(1, n + 1):
    value = float(input("Введите значение измерения:"))
    summ += value
average = summ / n
print("Сумма всех введённых значений:", summ)
print("Среднее арифметическое всех введённых значений:", average)









