# Порядок графа - число вершин(узлов).
# Размер графа - число рёбер.
# Способы хранения графа:
# 1) Множества вершин и рёбер
Vertexes = {'A', 'B', 'C', 'D'}
Edges = {('A', 'B'), ('B', 'C'), ('C', 'D')}

# 2) Матрица смежности
Vertexes = ['A', 'B', 'C', 'D']
indexes = {Vertexes[i]: i for i in range(len(Vertexes))}
# indexes = {}
# for i, x in enumerate(Vertexes):
#    indexes[x] = i
# print(indexes)

Matrix = [[0, 1, 0, 0],
          [1, 0, 1, 0],
          [0, 1, 0, 1],
          [0, 0, 1, 0]]

# 3) Списки смежности (Хеш-таблицы)
Graph = {'A': {'B'},
         'B': {'A', 'C'},
         'C': {'B', 'D'},
         'D': {'C'}}

import networkx as nx=
Graph = nx.Graph()
Graph.add_edge('A', 'B')
Graph.add_edge('B', 'C')
Graph.add_edge('C', 'D')

# Считывание графа и запись в матрицу смежности
# n - число вершин, m - число рёбер
'''
n, m = [int(x) for x in input().split()]
Vertexes = []
indexes = {}
Matrix = [[0] * n for i in range(n)]
for i in range(m):
    v1, v2 = input().split()
    for v in v1, v2:
        if v not in indexes:
            Vertexes.append(v)
            indexes[v] = len(Vertexes) - 1
    v1_i = indexes[v1]
    v2_i = indexes[v2]
    Matrix[v1_i][v2_i] = 1
    Matrix[v2_i][v1_i] = 1
'''
'''
# Считывание графа и запись в списки смежности
n, m = [int(x) for x in input().split()]
Graph = {}
for i in range(m):
    v1, v2 = input().split()
    if v1 not in Graph:
        Graph[v1] = set()
    if v2 not in Graph:
        Graph[v2] = set()
    Graph[v1].add(v2)
    Graph[v2].add(v1)
print(Graph)
'''
# Компактное хранение списков смежности для неизменяемого графа
import array

edges = array.array('u', ['B', 'A', 'C', 'B', 'D', 'C'])
offset = [0, 1, 3, 5, 6]
for i in range(len(offset) - 1):
    print(*edges[offset[i]:offset[i + 1]])