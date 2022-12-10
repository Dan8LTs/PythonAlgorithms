# binary search
# массив должен быть отсортирован по возрастанию
def left_bound(A, key):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] < key:
            left = middle
        else:
            right = middle
    return left


def right_bound(A, key):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] <= key:
            left = middle
        else:
            right = middle
    return right


M = [4, 5, 6, 8, 8]


def find(A, key):
    lb = left_bound(A, key)
    rb = right_bound(A, key)
    return rb - lb - 1


print(find(M, 8))


# Число Фиббоначи
def fib(n):
    if n <= 1:
        return n
    return (fib(n - 1) + fib(n - 2))


print(fib(9))


# Динамическое программирование

def fib_better(n):
    fib = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]


print(fib_better(15))


# задача про кузнечика: минимальная стоимость
def min_cost(N, price: list):
    C = [float("-inf"), price[1], price[1] + price[2]] + [0] * (N - 2)
    for i in range(3, N + 1):
        C[i] = price[i] + min(C[i - 1], C[i - 2])
    return C[N]


print(min_cost(5, [0, 5, 2, 10, 8, 6]))

# двумерный массив
# M - количество столбцов
# N - количество строк
M = 5
N = 5
A = [[0] * M for i in range(N)]
print(A[0] == A[1])
print(A[0] is A[1])  # проверяет: на один ли элемент указывают ссылки
