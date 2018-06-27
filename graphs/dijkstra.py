from collections import deque
import sys


#Ввод взвешенного графа

def read_weighted_graph():
	print("Вводите ребра с весом типа A B weight. stop означает прекратить ввод")
	G = {}
	user_input = input()
	while user_input != "stop":
		a, b, weight = user_input.split()
		weight = int(weight)
		if a not in G:
			G[a] = {b: weight}
		else:
			G[a][b] = weight
		user_input = input()
	
	return G


#Алгоритм Дийкстры для поиска кратчайшего расстояния	
		
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

#Запись взвешенного
	
def print_weighted_graph(filename,graph):
	file_graph = open(sys.path[0] + "\\" + filename + ".txt", "w")
	for key in graph:
		string = key + ":"
		for node in graph[key]:
			string = string + " " + node + "=%d" %(graph[key][node])
		string += "\n"
		file_graph.write(string)
	file_graph.close()
	
	
def get_weighted_graph_from_file(filename):	
	file_graph = open(sys.path[0] + "\\" + filename + ".txt", "r")
	graph = {}
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
		graph[key] = value
	file_graph.close()
	return graph

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


# G = get_weighted_graph_from_file("weighted_graph_1")
# start = input("С какой вершины начать?")
# while start not in G:
	# start = input("Такой вершины в графе нет. С какой вершины начать")
# shortest_distances = dijkstra(G,start)
# finish = input("К какой вершине построить путь?")
# while start not in G:
	# finish = input("Такой вершины в графе нет. К какой вершине построить путь?")
# shortest_path = recreate_shortest_path(G, start,finish, shortest_distances)









