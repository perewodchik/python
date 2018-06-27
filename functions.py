#Проверяет, является ли число простым. Выводит True если да, False если нет
def is_prime(x):
	"""Определяет, является ли число простым;
		x - целое положительное число
	"""
	divisor = 2
	while divisor < x:
		if x%divisor == 0:
			return False
		divisor += 1
	return True

#Раскладывает число на множители и выводит на экран
def factorize_number(x):
	"""Разложение числа на множители
		Печатает их на экран
	"""
	divisor = 2
	while x > 1:
		if x%divisor == 0:
			print(divisor)
			x //= divisor
		else:
			divisor += 1

#Находит факториал заданного натурального числа
def factorial(n):
	assert n>=0 , "ERROR"
	if n == 0:
		return 1
	return factorial(n-1)*n

#Находит наибольший общий делитель двух чисел. Оптимизированный алгоритм Евклида
def gcd(a,b):
	if b == 0:
		return a 
	return gcd(b, a%b)

#Медленный способ возведения в степень натурального числа в натуральную степень
def power_slow(a,n):
	assert n >= 0 , "ERROR" 
	if n == 0:
		return 1
	return power_slow(a,n-1)*a

#Оптимизированный способ возведения в степень натурального числа в натуральную степень
def power(a,n):
	assert n >= 0 , "ERROR" 
	if n == 0:
		return 1
	elif n%2 ==1:
		return power(a,n-1)*a
	else:
		return power(a*a,n//2)

#СУПЕР медленный и плохой способ нахождения чисел фибоначи. Не используй его!!!
def fibonacci_slow(n):
	if n == 1 or n == 2:
		return 1
	return fibonacci(n-1) + fibonacci(n-2)


#Динамическое программирование	
	
#Используй эту функцию нахождения чисел фибоначи, она топчик. 
def fibonacci(n):
	fib = [0,1] + [0]*(n-1)
	for i in range(2, n+1):
		fib[i] = fib[i-1]+fib[i-2]
	return fib[n-1]

#Посчитай минимальную стоимость прыжков кузнечика с командами +1 и +2
def count_min_cost(N, price:list):
	C = [float("-inf"), price[1], price[1]+price[2]]+[0]*(N-2)
	for i in range(3,N+1):
		C[i] = price[i] + min(C[i-1],C[i-2])
	return C[N]
		
#Растояние Левенштейна - минимальное редакционное расстояние, необходимое для превращения из одной строки в другую, используя только добавление символов, удаление или изменение. Сложность O(N*M)
def levenstein(A,B):

	F = [[(i+j) if i*j == 0 else 0 for j in range(len(B)+1)]for i in range(len(A) + 1)]
	for i in range(len(A) + 1 ):
		for j in range(1,len(B)+1):
			if A[i-1] == B[j-1]:
				F[i][j] = F[i-1][j-1]
			else:
				F[i][j] = 1 + min(F[i-1][j], F[i][j-1], F[i-1][j-1])
	return F[len(A)][len(B)]

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

	
#Генерирует числа в N-ричной системе счисления
def generate_numbers(N,M,prefix = None):
	""" Генерирует все числа в N-ричной
		системе счисления(N <=10
	"""
        
	prefix = prefix or []
	
	if M == 0:
		print(prefix)
		return
	
	for digit in range(N):
		prefix.append(digit)
		generate_numbers(N,M-1,prefix)
		prefix.pop()
	
#Создает перестановки N чисел в M позициях
def generate_permutations(N,M=-1,prefix = None):
	""" Генерирует перестановки N чисел в M позициях,
		с префиксом prefix
	"""
	M = N if M == -1 else M
	prefix = prefix or []
	if M == 0:
		print(*prefix, end=", ", sep="")
		return
	for number in range(1,N+1):
		if find(number,prefix):
			continue
		prefix.append(number)
		generate_permutations(N, M-1, prefix)
		prefix.pop()


		
#Структура данных - стэк:

import A_stack
	
#Проверка корректности скобочной последовательности
def parenthesis(string):
	"""
	Проверяет скобочное выражение
	
	>>> parenthesis("((()))")
	True
	>>> parenthesis("][")
	False
	>>> parenthesis("[(()])")
	False
	"""
	for brace in string:
		if brace not in "()[]":
			continue
		if brace in "([":
			A_stack.push(brace)
		else:
			assert brace in ")]", "Катастрофа! Ожидалась закрывающаяся скобка:" + str(brace)
			if A_stack.is_empty():
				return False
			left = A_stack.pop()
			assert left in "([", "Катастрофа! Ожидалась открывающая скобка:" + str(left)
			if left == "(":
				right = ")"
			elif left == "[":
				right = "]"
			if right != brace:
				return False
	return A_stack.is_empty()
	
#Обратная польская нотация. Алгоритм вычисления выражений в постфиксной нотации
def polish_notation(A):
	"""
	Обратная польская нотация. Алгоритм вычисления выражений в постфиксной нотации,
	На вход получает лист с числами и арифметическими действиями
	>>> polish_notation([2,7,"+",5,"*"])
	45
	>>> polish_notation([2,7,5,"*","+"])
	37
	>>> polish_notation([3,4,10,"-",20,"*","-"])
	117
	
	"""
	for k in A:
		if isinstance(k, int):
			A_stack.push(k)
		elif k in "+-*/":
			x = A_stack.pop()
			y = A_stack.pop()
			if k == "+":
				z = x + y
			if k == "-":
				z = x - y
			if k == "*":
				z = x * y
			if k == "/":
				z = x // y
			A_stack.push(z)
		else:
			continue
	return A_stack.pop() if A_stack.is_empty else "Случилось какое-то говно"

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
