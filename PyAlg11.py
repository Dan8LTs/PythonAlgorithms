# вычисление расстояния Левенштейна
def levenstein(A, B):
    i = 0
    j = 0
    F = [[(i + j) if i * j == 0 else 0 for i in range(len(B) + 1)] for i in range(len(A) + 1)]
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                F[i][j] = F[i - 1][j - 1]
            else:
                F[i][j] = 1 + min(F[i - 1][j], F[i][j - 1], F[i - 1][j - 1])
    return F[len(A)][len(B)]


print(levenstein('car', 'var'))


def equal(A, B):
    if len(A) != len(B):
        return False
    for i in range(len(A)):
        if A[i] != B[i]:
            return False
    return True


print(equal('hello', 'hey'))


def search_substr(S, sub):
    for i in range(len(S) - len(sub) + 1):
        if equal(S[i:i + len(sub)], sub):
            return i


print(search_substr('golang', 'go'))
