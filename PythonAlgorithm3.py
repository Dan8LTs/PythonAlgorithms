def program1():
	A = [1, 5, 7, 8]
	# x is an object reference
	for x in A:
		print(x, type(x))
		x += 1
	print(A)
program1()

def program2(A):
	for k in range(4):
		A[k] = A[k] * A[k]
		print(A[k], end=", ")

def program3(A):
	top = 0
	x = int(input())
	while x != 0:
		A[top] = x
		top += 1
		x = int(input())
	for k in range(4, -1, -1):
		print(A[k])

def program4():
	N = int(input())
	A = [0] * N
	B = [0] * N
	for k in range(N):
		A[k] = int(input())
	for k in range(N):
		B[k] = A[k]
	C = list[A]

def array_search(A:list, N:int, x:int):
	""" Осуществляет поиск числа х в массиве А от 0 до N-1 индекса включительно. 
	Возвращает индекс элемента x в массиве А. 
	Или -1, если такого нет.
	Если в массиве несколько одинаковых элементов, равных х, то вернуть индекс первого из них.
	"""
	for k in range(N):
		if A[k] == x:
			return k
	return -1

def test_array_search():
	A1 = [1, 2, 3, 4, 5]
	m = array_search(A1, 5, 4)
	if m == 3:
		print("#test1 - ok")
	else:
		print("#test1- fail")

	A2 = [-1, -2, -3, -4, -6]
	m = array_search(A2, 5, -8)
	if m == -1:
		print("#test2 - ok")
	else:
		print("#test2- fail")

	A2 = [20, 50, 30, 50, 80]
	m = array_search(A2, 5, 50)
	if m == 1:
		print("#test3 - ok")
	else:
		print("#test3- fail")
test_array_search()

def invert_array(A:list, N:int):
	""" Обращение массива """
	for k in range(N//2):
		A[k], A[N-1-k] = A[N-1-k], A[k]
	return A

def test_invert_array():
	M1 = [1, 2, 3, 4, 5]
	M1 = invert_array(M1, 5)
	print(M1)
	if M1 == [5, 4, 3, 2, 1]:
		print("#test1 - ok")
	else:
		print("#test1- fail")

def cyclic_shift_left():
	A = [0, 1, 2, 3, 4]
	N = 5
	tmp = A[0]
	for k in range(N - 1):
		A[k] = A[k+1]
	A[N - 1] = tmp
	print(A)

def cyclic_shift_right():
	A = [0, 1, 2, 3, 4]
	N = 5
	tmp = A[N-1]
	for k in range(N - 2, -1, -1):
		A[k+1] = A[k]
	A[0] = tmp
	print(A)

def Sieve_of_Eratosthenes():
	N = 5
	A = [True] * N
	A[0] = A[1] = False
	for k in range(2, N):
		if A[k]:
			for m in range(2*k, N, k):
				A[m] = False
	for k in range(N):
		print(k, '-', 'Простое' if A[k] else 'Составное')
		