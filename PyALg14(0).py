s = "Hi, Story!"
print(type(s))
# оператор присваивания - ссылка
s = 5+8+6
print(s)
a = 3
b = 5
# обмен значениями
a, b = b, a
print(a, b)
# каскадное присваивание
x = y = z = 0
z += 1
print(x, y, z)
# множественное присваивание
# арифметические операции
# ** возведение в степень
x = 5
x = x ** 2
print(x)
print(4 ** 0.5)
x = 6
y = 9
print(x * y)
print(x / y)
print(x % y)
print(x // y)
# python - не архитектурно-ориентированный я.п.
print(-15 // 8)
print(-15 % 8)
print()

# цикл while
# else выполняется после тела цикла
# break полностью завершает выполнение цикла
x = 0
while x < 8:
    x += 1
    if x % 2 != 0:
        continue
    print(x)
else:
    x = 88
    print(x)

for x in 1, 6, 3, 5:
    print(x ** 2, end=' ')

print()
for i in range(10, 1, -1):
    print(i, end = " ")