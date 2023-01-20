def dfs(vertex, graph, used):
    used.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour not in used:
            dfs(neighbour, graph, used)


used = set()
# количество компонент связности
n = 0
graph = {'A': {'B'},
         'B': {'A'},
         'C': {'D'},
         'D': {'C'}}
for vertex in graph:
    if vertex not in used:
        dfs(vertex, graph, used)
        n += 1
print(n)


# Алгоритм Косарайю используется для поиска компонент сильной связности.

# Топологическая сортировка. Алгоритм Тарьяна. O(n)
def dfs(start, graph, visited, ans):
    visited.add(vertex)
    for u in graph[start]:
        if u not in visited:
            dfs(u, graph, visited, ans)
    ans.append(start)


visited = set()
ans = []

for vertex in graph:
    if vertex not in visited:
        dfs(vertex, graph, visited, ans)
ans[:] = ans[::-1]
print(ans)
