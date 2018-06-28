#Задача о рюкзаке

"""
	Полный перебор - асимптотика O(2**N) - решает
	Жадный алгоритм - берем самый ценный - асимптотика O(N**2) - не всегда решает
	Оптимизированный жадный алгоритм - ценность делить на массу O(N**2) - 		не всегда решает
	
	дискретная задача о рюкзаке
	F(i,k) - максимальная стоимость, которая помещает в рюкзаке емкости k, при этом можно  использоваться первые i предметов 
	m[i] - массы
	v[i] - стоимость
	M - максимальная стоимость
"""

m = [1,3,6,2,2]
v = [3,2,5,6,5]
M = 10

def backpack_problem(mass,value, max_mass):
	assert len(mass) == len(value), "Количество предметов масс не равно количеству предметов ценности"
	#Создаем лист кортежей, первое число - масса, второе - ценность
	items = [None]*len(mass)
	
	for i in range(len(mass)):
		items[i] = (mass[i],value[i])
		
	N= len(items)
	F = [[0]*(N+1) for i in  range(max_mass+1)]

	for i in range(1,N+1):
		for k in range(1,max_mass+1):
			if items[i-1][0] <= k:
				F[k][i] = max(F[k][i-1], items[i-1][1] + F[k-items[i-1][0]][i-1])
			else:
				F[k][i] = F[k][i-1]
				
	return F[max_mass][N]) 