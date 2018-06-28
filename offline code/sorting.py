def insert_sort(A):
	""" сортировка списка А вставками """
	N = len(A)
	for top in range(1, N):
		k = top
		while k > 0 and A[k-1] > A[k]:
			A[k], A[k-1] = A[k-1], A[k]
			k -= 1

def choice_sort(A):
	""" сортировка списка А выбором """
	N = len(A)
	for pos in range(0, N-1):
		for k in range(pos+1, N):
			if A[k] < A[pos]:
				A[k], A[pos] = A[pos], A[k]
	
def bubble_sort(A):
	""" сортировка списка А методом пузырька """
	N = len(A)
	for bypass in range(1, N):
		for k  in range(0,N-bypass):
			if A[k] > A[k+1]:
				A[k], A[k+1] = A[k+1], A[k]

def merge(A: list, B: list):
	C = [0]*(len(A)+len(B))
	i = k = n = 0
	
	while i < len(A) and k < len(B):
		if A[i] < B[k]:
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
		
def merge_sort(A):
	"""Сортировка методом слияния
	"""
	if len(A) <= 1:
		return
	middle = len(A)//2
	L = [A[i] for i in range(0,middle)]
	R = [A[i] for i in range(middle, len(A))]
	merge_sort(L)
	merge_sort(R)
	C = merge(L,R)
	for i in range(len(A)):
		A[i] = C[i]
			
def hoar_sort(A):
	""" Сортировка методом Тони Хоара,
		Quick Sort
	"""
	if len(A) <= 1:
		return
	barrier = A[0]
	L = []
	M = []
	R = []
	for x in A:
		if x < barrier:
			L.append(x)
		elif x == barrier:
			M.append(x)
		else:
			R.append(x)
	k = 0
	hoar_sort(L)
	hoar_sort(R)
	for x in L+M+R:
		A[k] = x
		k += 1
					
def check_sorted(A, ascending=True):
	""" Проверка отсортированности за О(len(A))
	"""
	flag = True
	s = 2*int(Ascending) - 1
	for i in range(len(A)-1):
		if s*A[i] > s*A[i+1]:
			flag = False
			break
	return flag 
	
#Бинарный поиск. Выводит левый и правый индексы чисел между ним. 	
def left_bound(A, key):
	left = -1
	right = len(A)
	while right - left > 1:
		middle = (left+right)//2
		if A[middle] < key:
			left = middle
		else:
			right = middle
	return left

def right_bound(A, key):
	left = -1
	right = len(A)
	while right - left > 1:
		middle = (left+right)//2
		if A[middle] <= key:
			left = middle
		else:
			right = middle
	return right
			
