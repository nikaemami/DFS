# DFS
Implementing **DFS**, and **Random DFS** algorithms on different problems.

<h2>DFS</h2>

<h4>Soccer Teams:</h4>

We want to put a group of people into two soccer teams, where **people who don't like each other are not in the same team**.

Not liking each other is mutual, so if person A doesn't like person B, person B doesn't like person A either. We know that in each group of people, there are at least 2 people who don't like each other. The goal is to make **two teams with same number of members** where the above condition is satisfied, and the maximum number of people are playing.

INPUT: In the first line, two numbers n and m are given. n is the **total number of people**. m is the **number of dislikes **in between** them. In the next m line, the **pairs of people who don't like each other** are given.

OUTPUT: The minimum number of people who can't play soccer is printed.

**INPUT:**

6 6 

1 2 

2 3 

3 1 

4 5 

5 6

6 4

**OUTPUT:**

2

The key part of the code, is the DFS function implemented as below:

```ruby
def dfs(graph, node, visited, final_set):
    visited.append(node)
    final_set.append(node)
    for v in graph[node]:
        if v not in visited:
            final_set = dfs(graph, v, visited, final_set)
    return final_set
```

The next step is to find the cycles in the graph. This is implemented by using the 2 functions below, which first finds the connected components in a graph, and then finds the cycles from them:

```ruby
def find_connected (visited, graph)
def find_cycle(graph, connected)
```

The find_connected function is where the dfs algorithm is used.

<h2>Random DFS</h2>

The goal is to find the expected value of the **starting time** of a node, when implementing a random DFS algorithm on a vertex of a tree.

There is a tree with n vertices and m edges. We perform a random DFS algorithm, where in each recurrance of the DFS function, the neighbors list of vertex v is **shuffled**. Then the starting time for each vertex in saved. The goal is to find the **expected value** of the starting time.

INPUT: In the first line n is given as the number of the vertices in the graph. In the second line, n-1 numbers are given where the ith number, is the parent of vertex i .

OUTPUT: In a single line, n numbers are printed where the ith number, is the starting time of vertex i .

**INPUT:**

7 1 2 1 1 4 4

**OUTPUT:**

1.0 4.0 5.0 3.5 4.5 5.0 5.0

First, a recursive **dfs** function is implemented:

```ruby
def dfs(graph, v, time)
```

After implementing dfs on a random vertex, the expected of the starting time is implemented in the function below:

```ruby
def e_calc(graph, v, time, E):
    for i in range (len(graph[v])):
        E[graph[v][i]] = E[v] + 1 + (time[v]-time[graph[v][i]]-1)/2.0
        e_calc(graph, graph[v][i], time, E)
```


