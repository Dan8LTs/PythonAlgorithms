# Индуктивные функции. Однопроходный алгоритм.
A = [1, 4, 6, 7, 8]
# последовательность -> последовательность
# фильтрация
A = [x for x in A if x % 2 == 0]
print(A)
A = [x ** 2 for x in A]
print(A)
# последовательность -> число
# такие алгоритмы бывают однопроходные и не однопроходные
# fn+1 = F(fn, xn+1) - индуктивная функция
