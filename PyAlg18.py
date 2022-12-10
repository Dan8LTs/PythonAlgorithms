# именованные кортежи
import math, collections

A = (1, 0, 3)
print(math.sqrt(A[0] ** 2 + A[1] ** 2 + A[2] ** 2))

Point = collections.namedtuple("Point", "x y z")
# кортеж неизменяем
A = Point(1, 0, 3)
print(math.sqrt(A.x ** 2 + A.y ** 2 + A.z ** 2))

# односвязный список
# доступ к a[i] элементу за O(N)
a = [1]
a.append([2])
a[1].append([3, None])
p = a
while p is not None:
    print(p[0])
    p = p[1]
print()
# RAM - random access memory

# односвязный список помогает быстро вставлять элемент в начало или середину без переноса элементов
a = [0, a]
p = a
while p is not None:
    print(p[0])
    p = p[1]
print()


class LinkedList:
    def __init__(self):
        self._begin = None

    def insert(self, x):
        self._begin = [x, self._begin]

    def pop(self):
        assert self._begin is not None, "List is empty"
        x = self._begin[0]
        self._begin = self._begin[1]
        return x


L = LinkedList()
L.insert(5)
L.insert(10)
print(L.pop())
print()


class Heap:
    def __init__(self):
        self.values = []
        self.size = 0

    # O(log_n)
    def add(self, x):
        self.values.append(x)
        self.size += 1
        self.sift_down(0)
        self.sift_up(self.size - 1)

    # O(log_n)
    def sift_up(self, i):
        while i != 0 and self.values[i] < self.values[(i - 1) // 2]:
            self.values[i], self.values[(i - 1) // 2] = self.values[(i - 1) // 2], self.values[i]
            i = (i - 1) // 2

    # O(log_n)
    def extract_min(self):
        if not self.size:
            return None
        tmp = self.values[0]
        self.values[0] = self.values[-1]
        self.values.pop(0)
        self.size -= 1
        if self.size > 1:
            self.sift_up(self.size - 1)
            self.sift_down(0)
        return tmp

    # O(log_n)
    def sift_down(self, i):
        while 2 * i + 1 < self.size:
            j = i
            if self.values[2 * i + 1] < self.values[i]:
                j = 2 * i + 1
            if 2 * i + 2 < self.size and self.values[2 * i + 2] < self.values[i]:
                j = 2 * i + 2
            if i == j:
                break
            self.values[i], self.values[j] = self.values[j], self.values[i]
            i = j


h = Heap()
h.add(3)
h.add(5)
h.add(6)
h.add(8)
h.add(9)
h.add(7)
h.add(123123)
print(h.values)


# O(nlogn)
def get_sorted_array(heap):
    arr = []
    while heap.size != 0:
        arr.append(heap.extract_min())
    return arr


print(get_sorted_array(h))

ts = [52343, 23, 42, 32, 42, 342]

import heapq

ts = [52343, 23, 42, 32, 42, 342]
heapq.heapify(ts)
print(ts)


# O(nlogn)
def heapify(arr):
    heap = Heap()
    for item in arr:
        heap.add(item)
    return heap


print(heapify(ts).values)
