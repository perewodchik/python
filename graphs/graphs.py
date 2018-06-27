import sys
from collections import deque


#Создает граф и возвращает словарь. может быть ориентированным или неориентированным. 
#В ориентированном графе если у вершины нет ни одного исходоящего ребра, то у него пустое множество
def read_graph_list(oriented=False):
	print("\nВведите ребра по очереди через пробел. Напишите STOP, чтобы прекратить ввод")
	neighbors = {}
	while True:
		user_input = input()
		if user_input.upper() == "STOP":
			break
		vertex1, vertex2 = user_input.split()
		
		if oriented: #Создаем условия создания ориент/неориент графа
		
			if vertex1 not in neighbors:
				neighbors[vertex1] = {vertex2}
			else:
				neighbors[vertex1].add(vertex2)
			if vertex2 not in neighbors:
				neighbors[vertex2] = set()
		
		else:
		
			for v,u in (vertex1, vertex2), (vertex2, vertex1):
				if v not in neighbors:
					neighbors[v] = {u}
				else:
					neighbors[v].add(u)	
	
	return neighbors		
	

#Вывод в файл листами смежности
def print_to_file_list(filename,graph_dict):
	graph_adjacency_list = open(sys.path[0] + "\\" + filename + ".txt", "w")
	
	for key in graph_dict:
		string = ""
		for symbol in graph_dict[key]:
			string = string + symbol + " "	
		line = str(key + ': ' + string + '\n' )
		graph_adjacency_list.write(line)
	graph_adjacency_list.close()

#Вывод в файл взвешенного графа
def print_weighted_graph(filename,graph):
	file_graph = open(sys.path[0] + "\\" + filename + ".txt", "w")
	for key in graph:
		string = key + ":"
		for node in graph[key]:
			string = string + " " + node + "=%d" %(graph[key][node])
		string += "\n"
		file_graph.write(string)
	file_graph.close()	

#Получает граф и возвращает словарь в зависимости от типа графа типы графа. 
#Типы графов: Простой/ориентированный/взвешенный. обозначаются в названии файла
def get_graph_from_file(filename):
	if "num_" in filename: #Определяем, будем ли граф записан числами
		flag_number = True
	else: 
		flag_number = False
	
	if "weighted_" in filename:
		flag_weighted = True
	else:
		flag_weighted = False
	
	graph_dict = {}
	file_graph = open(sys.path[0] + "\\" + filename + ".txt", "r")
	if flag_weighted:
		for line in file_graph:
			string = line
			colon = string.find(":")
			key = string[0 : colon]
			value = {}
		
			for inner_string in string[colon + 1:].split():
				equal_sign = inner_string.find("=")
				inner_key = inner_string[0 : equal_sign]
				weight = int(inner_string[equal_sign + 1:])
				value[inner_key] = weight
			graph_dict[key] = value
	else:
		for line in file_graph: #Считываем соседей каждой вершины
			string = line
			colon = string.find(":")
			key = int(string[0: colon]) if flag_number else string[0: colon] #Ключ, который может быть числом или строкой
			value_set = set()
			for value in string[colon + 1:].split():
				if flag_number:
					value_set.add(int(value))
				else:
					value_set.add(value)
			graph_dict[key] = value_set
	file_graph.close()
	return graph_dict
	

	
#Обход в глубину
used = set()
def dfs(vertex, G):
	used.add(vertex)
	for neighbor in G[vertex]:
		if neighbor not in used:
			dfs(neighbor, G)

#поиск компонент связности			
def find_connected_component(G):
	N = 0
	for vertex in graph:
		if vertex not in used:
			dfs(vertex, graph)
			N += 1
	return N


#топологическая сортировка
visited = set()
ans = []
#N = len(graph)

def dfs_topology(start, G, visited):
	visited.add(start)
	if start in graph:
		for u in G[start]:
			if not u in visited:
				dfs_topology(u,G,visited)
		ans.append(start)
	
def topology_sort(graph):
	for vertex in graph:
		if vertex not in visited:
			dfs_topology(vertex,graph,visited)
	ans[:] = ans[::-1]
	return ans

#Обход в ширину

def bfs(starting_vertex):
	assert starting_vertex in graph, "Starting vertex not in graph!!!"
	distances = {}
	parents = {}
	for key in graph:
		distances[key] = None
	start_vertex = starting_vertex
	distances[start_vertex] = 0
	queue = deque([start_vertex])
	while queue:
		current_vertex = queue.popleft()
		for neighbor in graph[current_vertex]:
			if distances[neighbor] is None:
				distances[neighbor] = distances[current_vertex] + 1
				parents[neighbor] = current_vertex
				queue.append(neighbor)
	return distances, parents
	
#Возвращает словарь расстояний от заданной точки
def bfs_dist(starting_vertex):
	assert starting_vertex in graph, "Starting vertex not in graph!!!"
	distances = {}
	for key in graph:
		distances[key] = None
	distances[starting_vertex] = 0
	queue = deque([starting_vertex])
	while queue:
		current_vertex = queue.popleft()
		for neighbor in graph[current_vertex]:
			if distances[neighbor] is None:
				distances[neighbor] = distances[current_vertex] + 1
				queue.append(neighbor)
	return distances	

#Возвращает словарь предков, считая заданную точку главным
def bfs_parents(starting_vertex):
	assert starting_vertex in graph, "Starting vertex not in graph!!!"
	used = {}
	parents = {}
	for key in graph:
		used[key] = None
	parents[starting_vertex] = -1
	used[starting_vertex] = 0
	queue = deque([starting_vertex])
	
	while queue:
		current_vertex = queue.popleft()
		for neighbor in graph[current_vertex]:
			if used[neighbor] is None:
				used[neighbor] = 0
				parents[neighbor] = current_vertex
				queue.append(neighbor)
	return parents	

def find_path(parents, end_vertex):
	path = [end_vertex]
	parent = parents[end_vertex]
	while parent is not -1:
		path.append(parent)
		parent = parents[parent]
	return path[::-1]
	
def dijkstra(G, start):
	queue = deque([start])
	s = {}
	s[start] = 0
	while queue:
		v = queue.popleft()
		for u in G[v]:
			if u not in s or s[v] + G[v][u] < s[u]:
				s[u] = s[v] + G[v][u]
				queue.append(u)
	return s	
	
def recreate_shortest_path(G, start, finish, shortest_distances):
	path = [finish]
	i = 0
	while start not in path:
		for vertexes in  G[ path[i] ]:
			if shortest_distances[path[i]] - G[path[i]][vertexes] == shortest_distances[vertexes]:
				path.append(vertexes)
				i += 1
				break
	return path[::-1]
	

G = get_graph_from_file("weighted_graph_1")
start = input("С какой вершины начать?\n")
while start not in G:
	start = input("Такой вершины в графе нет. С какой вершины начать\n")
shortest_distances = dijkstra(G,start)
finish = input("К какой вершине построить путь?\n")
while start not in G:
	finish = input("Такой вершины в графе нет. К какой вершине построить путь?\n")
shortest_path = recreate_shortest_path(G, start,finish, shortest_distances)
print("Кратчайшее расстояние от вершины", start, "до вершины", finish, "равно", shortest_distances[finish])
print("Путь, по которому можно добраться до заданной вершины:\n", str(shortest_path).strip("[]"))

	
	
	
	
