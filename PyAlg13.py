# список хранит в себе ссылки на объекты
A = [3, 1.2, 32, "Hi!", True]
for x in A:
    print(type(x))
B = (3, 1.2, 32, A)
print(type(B))
# is проверяет, указывают ли ссылки на один объект
print(A[0] is B[0])
A[0] = 32
print(A[0] is A[2])
print(A[0] is B[0])

A = [(3, 4), (5, 2), (3, 8)]
for x, y in A:
    print(x, y)

# Строки
s = "Danil Maskin"
print(s.count('a'))
s.find("Dan")
s = """Мой дядя
самых честных правил"""
print(s)
s = "My name's Danil"
print(s)
s = "AAAAAA"
print(s.count("AAA"))
# Строки - НЕИЗМЕНЯЕМЫЕ объекты
# replace создаёт новую строку
t = s.replace("AAA", "BB")
print(t)
# Срезы строк
# Символ - строка единичной длины
s = "Tesla"
print(s[1: 4])
print(s[-1: -3: -1])
print(s[0:6:2])
# срез до края
print(s[0::2])
print(s[:])
A = [8, 12, 15, 32]
B = A[:]
print(B is A)
B = A
print(B is A)
print(A[::-1])
s = "sbcaacss"
x = s
s = s[::2] + s[::-2]
print(s)
print(x)

# Списки чисел
A[:3] = [5, 6, 64]
print(A)
A[:3] = []
print(A)
print(A[1000:2000])

A = [100, 32, 43, 56, 25]
A[::2] = [10, 20, 30]
print(A)
A[::2] = A[::-2]
print(A)

print(sum(A))
print(max(A))
print(min(A))

# Список строк
s = input("ФИО: ")
A = s.split()
print(A)
A[0] = A[0].upper()
print(A)
s = '+'.join(A)
print(s)
