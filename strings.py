# - минимальное редакционное расстояние, необходимое для превращения из одной строки в другую, используя только добавление символов, удаление или изменение. Сложность O(N*M)
def levenstein(A,B):
	F = [[(i+j) if i*j == 0 else 0 for j in range(len(B)+1)]for i in range(len(A) + 1)]
	for i in range(len(A) + 1 ):
		for j in range(1,len(B)+1):
			if A[i-1] == B[j-1]:
				F[i][j] = F[i-1][j-1]
			else:
				F[i][j] = 1 + min(F[i-1][j], F[i][j-1], F[i-1][j-1])
	return F[len(A)][len(B)]
	
#Наивный алгоритм равенства строк O(N)
def equal(A,B):
	if len(A) != len(B):
		return False
	for i in range(len(A)):
		if A[i] != B[i]:
			return False
	return True
	
#Поиск подстроки в строке(наивный)
def search_substring_slow(s, sub):
	for i in range(0,len(s)-len(sub)):
		if equal(s[i : i + len(sub)], sub):
			print(i)
			
#Префикс для алгоритма Кнутта-Морриса-Пратта
def prefix(string):
	M = [0]*len(string)
	i = j = 0
	for i in range(1, len(string)):
				while j > 0 and M[i] != M[j]:
					j = M[j-1]
				if string[j] == string[i]:
					M[i] = j + 1
					j += 1
	return M

#Поиск методом Кнутта-Морриса-Пратта
def search_kmp(string, sub_string):
	""" быстрый поиск методом Кнутта-Морриса-Пратта
		Сложность - О*(N+M)
	"""
	new_string = sub_string + "#" + string
	K = prefix(new_string)
	for i in range(0, len(new_string)):
		if K[i] == len(sub_string):
			return i - len(sub_string)*2 
	return -1
			
	

	
	