#При генерации чисел суммой меньше 1 среднее количество чисел будет равно e
from random import *
sum = 0
k = 0
N = 1_000_000
print("Generating numbers from 0 to 1 until their sum reaches 1 - ", N, "times")
for i in range(N):
	while sum < 1:
		sum += random()
		k += 1
	sum = 0
print("Average amount of random numbers required to reach 1 is",k/N)
	
