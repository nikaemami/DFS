from collections import defaultdict

numbers = list(map(int,input().split()))
n = numbers[0]
m = numbers[1]

graph = defaultdict(list)
for i in range(n):
    graph[i] = []

for i in range (m):
    enemy = list(map(int,input().split()))
    graph[int(enemy[0])-1].append(int(enemy[1]) - 1)
    graph[int(enemy[1])-1].append(int(enemy[0]) - 1)

final_set = []
visited = []

def dfs(graph, node, visited, final_set):
    visited.append(node)
    final_set.append(node)
    for v in graph[node]:
        if v not in visited:
            final_set = dfs(graph, v, visited, final_set)
    return final_set

def find_connected (visited, graph):
	connected = []
	for node in graph:
		if (node not in visited):
			final_set = []
			dfs_fcn = dfs(graph, node, visited, final_set)
			connected.append(dfs_fcn)
	return connected

connected = find_connected(visited, graph)

for component in connected:
    if (len(component) % 2 == 0):
        connected.remove(component)

def find_cycle(graph, connected):
    cycles = []
    for component in connected:
        condition = 1
        for node in component:
            if len(graph[node]) < 2:
                cycles.append(0)
                condition = 0
                break
        if (condition == 1):
            cycles.append(1)
    return cycles

cycles = find_cycle(graph, connected)

count = 0
for i in range (len(cycles)):
    if(cycles[i] == 0):
        count+=1
count = int(count / 2) * 2
print(len(cycles) - count)
