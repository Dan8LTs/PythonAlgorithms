""" Вычисление хеша по алгоритму sha256
import hashlib
def get_hash(data):
    return hashlib.sha256(str(data).encode()).hexdigest()
"""


def get_hash(data):
    k = 3571
    s = 0
    i = 1
    data += 84832941

    while data > 0:
        s += data % 2 * k ** i
        i += 1
        data //= 2

    return s % 2 ** 7


print(get_hash(234334))


# двухсвязный
class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def search(self, el):
        current = self.head

        while current is not None:
            if current[0] == el:
                return True
            current = current[1]
        return False

    def add(self, el):
        if not self.search(el):
            node = [el, None]
            if self.head is None:
                self.head = node
            else:
                self.tail[1] = node
            self.tail = node


l = LinkedList()
l.add(4)
l.add(26)
l.add(256)
l.add(32)
# удаление 4
l.head = l.head[1]
l.add(128)
print(l.head)


class HashTable:
    def __init__(self):
        self.table = [LinkedList() for _ in range(128)]

    def add(self, el):
        hash = get_hash(el)
        self.table[hash].add(el)

    def search(self, el):
        hash = get_hash(el)
        return self.table[hash].search(el)


ht = HashTable()
ht.add(8)
ht.add(6)
for i in ht.table:
    if i.head is not None:
        print(i.head, end=' ')
print()
print(ht.search(8))
