# Двоичное дерево - корневое дерево, где у любой вершины не более 2 дочерних
# Высота дерева - максимальное количество рёбер от корня до листа
# Двоичное дерево поиска - это структура данных, хранящая в вершинах элементы, содержащие упорядоченные ключи.
# пример реализации звена двоичного дерева
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.parent = None
        self.left = None
        self.right = None