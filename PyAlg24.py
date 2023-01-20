# Создаём очередь, неэффективная реализация
class queue:
    def __init__(self, q=[]):
        self.q = q

    def remove(self):
        self.q.pop(0)

    def add(self, el):
        self.q.append(el)

    def __str__(self):
        return str(self.q)


q = queue([100, 32, 80, 128, 256])
q.add(800)
q.remove()
print(q)

# Обход графа в ширину (Breadth-first searсh)
graph = {0: {1, 4},
         1: {0, 3, 4},
         2: {3, 4},
         3: {1, 2},
         4: {0, 1, 2}}

from collections import deque

start = 0
queue = deque([start])
distances = [None] * 5
distances[start] = 0

parents = [None] * 5

while queue:
    v = queue.popleft()
    for n in graph[v]:
        if distances[n] is None:
            distances[n] = distances[v] + 1
            parents[n] = v
            queue.append(n)
for i in distances:
    ind = distances.index(i)
    print("distance to vertex #", ind, ": ", i, ", parent:", parents[ind])

end = 3
path = [end]
parent = parents[end]
while not parent is None:
    path.append(parent)
    parent = parents[parent]
print(path[::-1])

# задача про коня на шахматной доске
letters = "abcdefgh"
numbers = "12345678"
graph = {}
for l in letters:
    for n in numbers:
        graph[l + n] = set()


def add_edge(v1, v2):
    graph[v1].add(v2)
    graph[v2].add(v1)


for i in range(8):
    for j in range(8):
        v1 = letters[i] + numbers[j]
        v2 = ''
        if 0 <= i + 2 < 8 and 0 <= j + 1 < 8:
            v2 = letters[i + 2] + numbers[j + 1]
            add_edge(v1, v2)
        if 0 <= i + 1 < 8 and 0 <= j + 2 < 8:
            v2 = letters[i + 1] + numbers[j + 2]
            add_edge(v1, v2)
        if 0 <= i - 2 < 8 and 0 <= j + 1 < 8:
            v2 = letters[i - 2] + numbers[j + 1]
            add_edge(v1, v2)
        if 0 <= i - 1 < 8 and 0 <= j + 2 < 8:
            v2 = letters[i - 1] + numbers[j + 2]
            add_edge(v1, v2)

for i, j in graph.items():
    print(i, ":", j)

# обход в ширину для задачи про шахматы
distances = {v: None for v in graph}
parents = {v: None for v in graph}

start = 'd4'
end = 'f7'

queue = deque([start])
distances[start] = 0

while queue:
    v = queue.popleft()
    for n in graph[v]:
        if distances[n] is None:
            distances[n] = distances[v] + 1
            parents[n] = v
            queue.append(n)

path = [end]
parent = parents[end]
while not parent is None:
    path.append(parent)
    parent = parents[parent]
print(path[::-1])