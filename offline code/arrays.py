# A = [5,2,3,4,6]
# print(A)
# for x in range(5):
	# print(A[x])

# B = [0]*1000
# top = 0
# x = int(input())
# while x != 0:
	# B[top] = x
	# top += 1
	# x = int(input())

# for k in range(top-1,-1,-1):
	# print(B[k])

# N = int(input())
# C = [0]*N
# D = [0]*N
# for k in range(N):
	# C[k] = int(input())
# for k in range(N):
	# D[k] = C[k]

# #List comprehensions
# A = [x**3 for x in range(3, 15,3)]

# #Создание двумерного массива через list comprehensions
# A = [[0]*M for i in range(N)]	
	
#Поиск элемента в массиве до индекса
def array_search(A:list, N:int, x:int):
	""" Осуществляет поиск числа х в массиве А
		от 0 до N-1 индекса включительно.
		Возвращает индекс элемента х в массиве А.
		Или -1, если такого нет.
		Если в массиве несколько одинаковых элементов,
		равных х, то вернуть индекс первого по счёту.
	"""
	for k in range(N):
		if A[k] == x:
			return k
	return -1

def test_array_search():
	A1 = [1,2,3,4,5]
	m = array_search(A1, 5, 8)
	if m == -1:
		print("#test1 - ok")
	else: 
		print("#test1 - fail")
		
	A2 = [-1,-2,-3,-4,-5]
	m = array_search(A2, 5, -3)
	if m == 2:
		print("#test2 - ok")
	else: 
		print("#test2 - fail")
		
	A3 = [10,20,30,10,10]
	m = array_search(A3, 5, 10)
	if m == 0:
		print("#test3 - ok")
	else: 
		print("#test3 - fail")

#Переворачивание массива		
def invert_array(A, N):
	""" Обращение массива (поворот задом-наперёд)
		в рамках индексов от 0 до N-1
	"""
	for k in range(N//2):
		A[k],A[N-1-k] = A[N-1-k],A[k]

def test_invert_array():
	A1 = [1,2,3,4,5]
	print(A1)
	invert_array(A1,5)
	print(A1)
	if A1 == [5,4,3,2,1]:
		print("#test1 - ok")
	else: 
		print("#test1 - fail")
		
	A2 = [0,0,0,0,0,10]
	print(A2)
	invert_array(A2,6)
	print(A2)
	if A2 == [10,0,0,0,0,0]:
		print("#test2 - ok")
	else: 
		print("#test2 - fail")

#Сдвиг массива влево
def cycle_copy_left(A,N):
	tmp = A[0]
	for k in range(N-1):
		A[k] = A[k+1]
	A[N-1] = tmp
	
def test_cycle_copy_left():
	A1 = [1,2,3,4,5]
	print(A1)
	cycle_copy_left(A1,5)
	print(A1)
	if A1 == [2,3,4,5,1]:
		print("test1 - ok")
	else:
		print("test1 - fail")

#Сдвиг массива вправо
def cycle_copy_right(A,N):
	tmp = A[N-1]
	for k in range(N-1,0,-1):
		A[k] = A[k-1]
	A[0] = tmp
	
def test_cycle_copy_right():
	A1 = [1,2,3,4,5]
	print(A1)
	cycle_copy_right(A1,5)
	print(A1)
	if A1 == [5,1,2,3,4]:
		print("test1 - ok")
	else:
		print("test1 - fail")

	
#Ищет число в листе
def find(number,A):
	""" Ищет x в А и возвращает True если такой есть
		False, если такого нет
	"""
	for x in A:
		if number == x:
			return True
	return False

#Классная сортировка методом Тони Хоара. Средняя сложность O(logN), но может дойти и до O(N**2) в самом худшем случае
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

#Слияние двух массивов в порядке возрастания. Нужно, в основном, только для сортировки слиянием
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
		
#Сортировка слиянием. Тоже классная, но требует дополнительной памяти. Сложность O(logN)
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


#Largest common subsequence - наибольшая общая подпоследовательность
def lcs(A,B):
	F = [[0]*(len(B) + 1) for i in range(len(A) + 1)]
	for i in range(1, len(A) + 1):
		for j in range(1, len(B) + 1):
			if A[i-1] == B[j-1]:
				F[i][j] = 1 + F[i-1][j-1]
			else:
				F[i][j] = max(F[i-1][j], F[i][j-1])
	return F[-1][-1]
		
#Наибольшая возрастающая подпоследовательность - нужно отсортировать данную подпоследовательность и найти наибольшую общую подпоследовательность между ними
def las(A):
	B = []
	for i in range(len(A)):
		B.append(A[i])
	hoar_sort(B)
	return lcs(A,B)

	
#Бинарный поиск - выводит левый и правый индексы чисел между ним. 	

#Левая граница бинарного поиска
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

#Правая граница бинарного поиска
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

	
	

