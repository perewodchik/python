#Задача - даны две точки на шахматном поле. Нужно найти кратчайший путь коня из одной точки в другую
from collections import deque
letters = 'abcdefgh'
numbers = '12345678'
graph = dict()

starting_vertex = 'd4'
end_vertex = 'f7'

def add_edge(v1,v2):
	graph[v1].add(v2)
	graph[v2].add(v1)

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

for l in letters:
	for n in numbers:
		graph[l+n] = set()
		
for i in range(8):
	for j in range(8):
		v1 = letters[i] + numbers[j]
		if 0 <= i + 2 < 8 and 0 <= j + 1 < 8:
			v2 = letters[i+2] + numbers[j+1]
			add_edge(v1,v2)
		
		if 0 <= i - 2 < 8 and 0 <= j + 1 < 8:
			v2 = letters[i-2] + numbers[j+1]
			add_edge(v1,v2)
			
		if 0 <= i + 1 < 8 and 0 <= j + 2 < 8:
			v2 = letters[i+1] + numbers[j+2]
			add_edge(v1,v2)
		
		if 0 <= i - 1 < 8 and 0 <= j + 2 < 8:
			v2 = letters[i-1] + numbers[j+2]
			add_edge(v1,v2)
				
starting_vertex = 'd4'
end_vertex = 'f7'

parents = bfs_parents(starting_vertex)
path = find_path(parents, end_vertex)
print(path)











