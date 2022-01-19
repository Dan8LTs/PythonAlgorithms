"""
A = [0] * N_max
n = 0
x = int(input())
A[n] = x
n += 1
n -= 1
x = A[n] 
"""

A= []
x = int(input())
A.append(x)
n = len(A)
x = A.pop()

"""
A = []
for x in range(10):
	A.append(x**2)
"""
A = [x**2 for x in range(10)]

"""
B = []
A = [1, 2, 3, 4, 5, 6]
for x in A:
	if x % 2 == 0:
		B.append(x**2)
"""
B = [x**2 for x in A if x % 2 == 0]

# Сортировка подсчётом
N = int(input())
F = [0] * 10
for i in range(N):
	x = int(input())
	F[x] += 1

