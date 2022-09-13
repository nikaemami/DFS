from collections import defaultdict

n = int(input())
p = list(map(int,input().split()))

graph = defaultdict(list)

for i in range(n):
    graph[i] = []

for i in range(len(p)):
    graph[p[i]-1].append(i+1)

time = [0] * n
def dfs(graph, v, time):
    time[v]=0
    for i in range (len(graph[v])):
        dfs(graph, graph[v][i], time)
        time[v]+=time[graph[v][i]]
    time[v]+=1

dfs(graph, 0, time)

E = [0] * n
def e_calc(graph, v, time, E):
    for i in range (len(graph[v])):
        E[graph[v][i]] = E[v] + 1 + (time[v]-time[graph[v][i]]-1)/2.0
        e_calc(graph, graph[v][i], time, E)

e_calc(graph, 0, time, E)

for i in range (n):
    E[i]+=1
for i in range (n):
    print(format(E[i],".1f"),end = ' ')