def merge(A: list, B: list):
	# Merge of sorted arrays
	C = [0] * (len(A) + len(B))
	i=k=n=0
	while i < len(A) and k < len(B):
		if A[i] <= B[k]:
			C[n] = A[i]
			i += 1
			n += 1
		else:
			C[n] = B[k]
			k += 1 
			n += 1
	while i < len(A):
		C[n] = A[i]
		i += 1
		n += 1
	while k < len(B):
		C[n] = B[k]
		k += 1
		n += 1
	return C

# A sort is said to be stable if it does not change the order of equal elements

def merge_sort(A):
	# Merge sort
	if len(A) <= 1:
		return 
	middle = len(A) // 2
	L = [A[i] for i in range(middle)]
	R = [A[i] for i in range(middle, len(A))]
	merge_sort(L)
	merge_sort(R)
	C = merge(L, R)
	for i in range(len(A)):
		A[i] = C[i]

M = [9, 1, 6, 6, 8, 7]
merge_sort(M)
print(*M)


def quick_sort(A):
	# Sorting by Tony Hoare
	if len(A) <= 1:
		return
	barrier = A[0]
	Less = []
	Equal = []
	More = []
	for x in A:
		if x < barrier:
			Less.append(x)
		elif x == barrier:
			Equal.append(x)
		else:
			More.append(x)
	quick_sort(Less) 
	quick_sort(More)
	k = 0
	for x in Less + Equal + More:
		A[k] = x
		k += 1

M2 = [9, 1, 6, 6, 8, 7]
quick_sort(M2)
print(*M2)

def check_sorted(A, ascending=True):
	# Quick check if an array is sorted
	flag = True
	s = 2 * int(ascending) - 1
	for i in range(len(A) - 1):
		if s * A[i] > s * A[i+1]:
			flag = False
			break
	return flag
print(check_sorted(M2))
print(check_sorted([5, 3, 6]))