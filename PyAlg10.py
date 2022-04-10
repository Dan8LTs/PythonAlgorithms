# Длина наибольшей общей подпоследовательности
def lcs(A, B):
	F = [[0]*(len(B)+1) for i in range(len(A)+1)]
	for i in range(1, len(A)+1):
		for j in range(1, len(B)+1):
			if A[i-1]==B[j-1]:
				F[i][j]=1+F[i-1][j-1]
			else:
				F[i][j]=max(F[i-1][j], F[i][j-1])
	return F[-1][-1]
print(lcs("hello", "cellos"))

# Длина наибольшей возрастающей подпоследовательности
def gis(A):
	F = [0] * (len(A)+1)
	for i in range(1, len(A)+1):
		m = 0 
		for j in range(0, i):
			if A[i-1] > A[j-1] and F[j] > m:
				m = F[j]
		F[i] = m + 1
	return max(*F)
print(gis([6, 2, 5]))
