def insert_sort(A):
    """Сортировка списка вставками"""
    for top in range(1, len(A)):
        k = top
        while k > 0 and A[k - 1] > A[k]:
            A[k], A[k - 1] = A[k - 1], A[k]
            k -= 1


def selection_sort(A):
    """Сортировка списка выбором"""
    for pos in range(0, len(A) - 1):
        for k in range(pos + 1, len(A)):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]


def bubble_sort(A):
    """Сортировка списка методом пузырька"""
    for bypass in range(1, len(A)):
        for k in range(0, len(A) - bypass):
            if A[k] > A[k + 1]:
                A[k], A[k + 1] = A[k + 1], A[k]


def test_sort(sort_algorithm):
    print("Тестируем: ", sort_algorithm.__doc__)
    print("test #1: ", end="")
    A = [4, 2, 3, 3, 1, 5]
    A_sorted = [1, 2, 3, 3, 4, 5]
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")

    print("test #2: ", end="")
    A = list(range(10, 20)) + list(range(0, 10))
    A_sorted = list(range(20))
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")


if __name__ == "__main__":
    test_sort(insert_sort)
    test_sort(selection_sort)
    test_sort(bubble_sort)
