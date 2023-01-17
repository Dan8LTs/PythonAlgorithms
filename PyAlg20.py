# Коллекция       | Особенности
# tuple ()        | x, y = f(x, y); x, y = y, x
# list []         | a.append(x); a[i] за O(1)
# set set(), {a}  | хеш-таблица => работа за O(1) и неупорядоченность
# dict {}, {a: b} | хеш-таблица => работа за O(1) и неупорядоченность

a = {1}
print(type(a))
a.pop()
print(a)

# в множество можно поместить любой итерируемый объект
b = set("qw3rty")
print(b)
print('q' in b)
b.add(1)
# b.discard("i") # Не выдаёт ошибки при отсутствии элемента
# b.remove("i") # KeyError 'i'
# удаление рандомного элемента
m = b.pop()

# Операции над множествами
A = set(range(0, 10, 2))
B = set(range(8, -1, -1))

print(A, " ", B)
print(A | B)
print(A & B)
print(B - A)
print(A ^ B)

print()

print(A >= B)
print(A <= B)
print(A > B)
print(A < B)
print(A == B)

# Ассоциативные массивы
D = {}
D = dict()
# словарь хранит связку ключ:значение
A = [0, 1, 2]
B = [12, 44, 64]
C = dict(zip(A, B))
C[3] = 15
if 4 in C:
    # без проверки будет KeyError
    print(C[4])
print(C)

# KeyError при отсутствии элемента
del C[3]
# удаляет и записывает в x элемент по ключу, если не найден - присваивает значение по умолчанию -1
x = C.pop(5, -1)
print(C)
print(x)

print("keys: ", end='')
for key in C:
    print(key, end='; ')
print()
print("values: ", end='')
for value in C.values():
    print(value, end='; ')

votes = {}
N = int(input())
for i in range(N):
    name = input()
    # if name in votes:
    #    votes[name] += 1
    # else:
    #    votes[name] = 1

    # Красиво, но хуже асимптотически
    votes[name] = votes.pop(name, 0) + 1
v = list(votes.items())
m = max(list(votes.values()))
for i in v:
    if i[1] == m:
        print(i[0])
