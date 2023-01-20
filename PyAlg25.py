# Алгоритм Дейкстры (поиск кратчайших путей между начальной и другими вершинами во взвешенном графе)
# Работает только с неотрицательными весами за время O(N^2)

graph = {'A': {'B': 4},
         'B': {'A': 6, 'C': 8},
         'C': {'B': 12, 'D': 15},
         'D': {'C': 26}}
distances = {}
start = 'A'
distances[start] = 0

from collections import deque

queue = deque()
queue.append(start)

while queue:
    c = queue.popleft()
    for n in graph[c]:
        if not n in distances or distances[c] + graph[c][n] < distances[n]:
            distances[n] = distances[c] + graph[c][n]
            queue.append(n)
print(distances)

# Алгоритм Флойда-Уоршелла, O(N^3)
# Основан на методе динамического програмирования
# Находит кратчайшее расстояние от каждой к каждой
# Работает с отрицательными весами, но не циклами отрицательного веса
