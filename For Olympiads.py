import timeit

s1 = timeit.default_timer()

k, n = (map(int, input().split()))
print(k, n)
def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n
#print(factorial(32))



s2 = timeit.default_timer()
def dynamic_factorial(n):
    l = [0] * (n + 1)
    l[0] = 1
    for i in range(1, n+1):
        l[i] = l[i-1] * i
    return l[i]
#print(dynamic_factorial(32))

#print(timeit.default_timer() - s1)

vertexes = [0] * 7
edges = []
for i in range(1, 8):
    vertexes[i-1] = i
print(vertexes)

edges.append([1, 2, 15])
edges.append([2, 5, 8])
edges.append([2, 6, 3])
edges.append([5, 6, 1])
edges.append([6, 5, 1])
edges.append([1, 3, 7])
edges.append([3, 4, 4])

matrix = [[0] * len(vertexes) for _ in range(len(vertexes))]
for e in edges:
    matrix[e[0] - 1][e[1] - 1] = e[2]
for m in matrix:
    print(*m)

count_connected_vertex_list = [0] * len(vertexes)
for e in edges:
    count_connected_vertex_list[e[0] - 1] += 1

def get_connected_vertex_list(v1):
    l = []
    for e in edges:
        if e[0] == v1:
            l.append(e[1])
    return l
print(count_connected_vertex_list)
print(get_connected_vertex_list(1))

def wave(start, finish):
    res = []
    res.append(start)
    list = []
    vertex = start
    for v in get_connected_vertex_list(vertex):
        list.append(v)
        verte
    return res