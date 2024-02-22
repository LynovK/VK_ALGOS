def dfs(grath, v, visited, color):
    visited[v] = color
    for i in grath[v]:
        if visited[i] == 0:
            dfs(grath, i, visited, color)

def find_connected_components(graph):
    visited = map[int]int
    for i in range(1, len(graph)):
        visited[i] = 0
    color = 0
    for i in range(1, len(graph)):
        currentNode = graph[i]
        if visited