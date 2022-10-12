# Use case:
# Описание структуры данных
"""
>>> clear()
>>> is_empty()
True
>>> push(1)
>>> push(2)
>>> push(3)
>>> is_empty()
False
>>> pop()
3
>>> pop()
2
>>> pop()
1
>>> is_empty()
True
"""

_stack = []


def push(x):
    """
    Добавление элемента x в конец списка
    >>> size = len(_stack)
    >>> push(5)
    >>> len(_stack) - size
    1
    >>> _stack[-1]
    5
    """
    _stack.append(x)


def pop():
    return _stack.pop()


def clear():
    _stack.clear()


def is_empty():
    return len(_stack) == 0


def is_braces_sequence_correct(s):
    """
    Проверям последовательность круглых и квадратных скобок
    >>> is_braces_sequence_correct("(([()]))[]")
    True
    >>> is_braces_sequence_correct("[(])")
    False
    >>> is_braces_sequence_correct("(")
    False
    >>> is_braces_sequence_correct("]")
    False
    """
    for current in s:
        if current not in "()[]":
            continue
        if current in "([":
            push(current)
        else:
            assert current in ")]", "Ожидалась закрывающая скобка: " + str(current)
            if is_empty():
                return False
            left = pop()
            assert left in "([", "Ожидалась открывающая скобка: " + str(current)
            if left == "(":
                right = ")"
            elif left == "[":
                right = "]"
            if right != current:
                return False
    return is_empty()

clear()
# обратная польская нотация
# [2, 6, 8, -, /] <==> (8-6)/2
def opn(s):
    """
    >>> opn([2, 8, 6, "-","/"])
    1.0
    """
    for token in s:
        if str(token) in "1234567890":
            push(token)
        else:
            y = pop()
            x = pop()
            z = eval(str(x) + token + str(y))
            push(z)
    return pop()
print(opn([2, 7, "+", 5, "*"]))
 #тесты
if __name__ == '__main__':
    import doctest
    doctest.testmod()
