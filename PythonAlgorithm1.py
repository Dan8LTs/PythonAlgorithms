print("пропустить программу - enter")
print("Проверка есть ли в последовательности число кратное 10")
found = False
f = input("Введите количество чисел: ")
if  f != "":
	count = int(f)
	for i in range(count):
		n = int(input(f"Введите число №{i + 1}:"))
		found = (n % 10 == 0) or found
	print(found)
print()

print("Проверка все ли числа в последовательности кратны 10")
found = True
f = input("Введите количество чисел: ")
if  f != "":
	count = int(f)
	for i in range(count):
		n = int(input(f"Введите число №{i + 1}:"))
		found = ((n % 10 == 0) and 
						found)
	print(found)
print()

print("Кратность 2, 3 и 6")
f = input("Введите число: ")
if  f != "":
	x = int(f)
	o = x % 3 == 0
	t = x % 2 == 0
	if o and t:
		print("Кратно 6")
	elif o:
		print("Кратно 3")
	elif t:
		print("Кратно 2")
print()

print("ABCD")
f = input("Введите число: ")
if  f != "":
	x = int(f)
	if x < 0:
		print("A")
	elif x < 5:
		print("B")
	elif x < 10:
		print("C")
	elif x >= 10:
		print("D")
	else:
		print("ERROR")
print()

print("I, II, III, IV")
x = int(input("Введите x: "))
y = int(input("Введите y: "))
if y > 0:
	if x > 0:
		print("I")
	else:
		print("II")
else:
	if x < 0:
		print("III")
	else:
		print("IV")
