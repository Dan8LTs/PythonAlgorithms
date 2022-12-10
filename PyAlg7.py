# generation of all possible permutations in the number system based Radix
def generate_numbers(Radix: int, NumbersAmount: int, prefix=None):
    prefix = prefix or []
    if NumbersAmount == 0:
        print(prefix)
        return
    for digit in range(Radix):
        prefix.append(digit)
        generate_numbers(Radix, NumbersAmount - 1, prefix)
        prefix.pop()


generate_numbers(2, 2)


# looking for a number in A
def find(number, A):
    for x in A:
        if number == x:
            return True
    return False


def generate_permutations(N: int, M: int = -1, prefix=None):
    # generating all permutations of N numbers in M positions with a prefix
    M = N if M == -1 else M
    prefix = prefix or []
    if M == 0:
        print(*prefix)
        return
    for number in range(1, N + 1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(N, M - 1, prefix)
        prefix.pop()
# generate_permutations(5, 5)
