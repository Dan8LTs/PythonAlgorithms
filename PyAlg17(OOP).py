# Классы и объекты
class Goat:
    # классовый атрибут не может быть изменяемым
    legs_num = 4
    # конструктор
    def __init__(self, horns, height):
        self.horns = horns
        self.height = height
    def __str__(self):
        s = 'height = {}, horns = {}, legs_num = {}'.format(self.height, self.horns, self.legs_num)
        return s
marusya = Goat(1, 100)
print(type(marusya))
print(marusya.legs_num)
# нельзя
# marusya.horns = 2
# notka.bell = 'Big'
notka = Goat(2, 120)
for x in marusya, notka:
    print(x)
# n ссылается на notka
n = notka
n.height += 5
print(n)
print(notka)

class Empty:
    pass