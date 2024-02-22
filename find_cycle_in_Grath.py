def has_cycle(grath):
    visited = []
    for vertex in grath:
        if vertex not in visited:
            if dfs(grath, vertex, None, visited):
                return True
    return False


def dfs(grath, vertex, parent, visited):
    visited.append(vertex)
    for nieghbor in grath[vertex]:
        if visited[i] == 0:

    return False
