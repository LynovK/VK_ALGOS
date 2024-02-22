def is_Tree(grath, start):
    visited = []
    queue = [start]
    parent = {start: None}

    while queue:
        vertex = queue.pop()
        visited.append(vertex)
        for nieghbor in grath[vertex]:
            #для узлов F и А
            if nieghbor not in visited:
                queue.append(nieghbor)
                parent[nieghbor] = vertex
            else:
                if parent[vertex] != nieghbor:
                    return False

    return len(visited) == len(grath)