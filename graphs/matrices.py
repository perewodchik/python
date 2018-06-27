import sys

#Вывод в файл матрицей смежности

print("Будет ли граф ориентированным? Y - будет, все остальное - нет: ", end="")
org_graph = True if input() == "Y" else False

# print("Введите количество используемых точек:", end=" ")
# N = int(input())
# index = {vertexes[i]:i for i in range(len(vertexes))}
index = {}
edges_list = [[0]]
for_index = 0

print("\nВведите ребра по очереди через пробел. Напишите STOP, чтобы прекратить ввод")
while True:
	user_input = input()
	if user_input.upper() == "STOP":
		break
	vertex1, vertex2 = user_input.split()
	
	for v in vertex1,vertex2:
		if v not in index:
			for_index += 1
			index[v] = for_index - 1
	
	while for_index != len(edges_list):
		edges_list.append([0]*len(edges_list))
		
	for i in range(for_index):
		while len(edges_list[i]) != for_index:
			edges_list[i].append(0)
		
				
			
	v1_i = index[vertex1]
	v2_i = index[vertex2]
	edges_list[v1_i][v2_i] += 1
	if not org_graph:
		edges_list[v2_i][v1_i] += 1
		
print(*edges_list, sep='\n')


adjacency_matrice = open(sys.path[0] + "\\adjacency_matrice", "w")
adjacency_matrice.write("oriented=" + str(org_graph) + '\n')
for i in range(len(edges_list)):
	adjacency_matrice.write(str(edges_list[i])+ '\n')
adjacency_matrice.close()