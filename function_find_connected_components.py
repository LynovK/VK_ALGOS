grath = {1:[2,3], 2:[1,3], 3:[1,2], 4:[6,7], 5:[6,7], 6:[4,5,7], 7:[4,5,6], 8:[11], 9:[10,11], 10:[9], 11:[8,9]}
def function_find_connected_components(grath):
    visited = map[int]bool
    for i in range(1,len(grath)):
        visited[i] = False
    connected_components = []
    for i in range(1, len(grath)):
        currentNode = grath[i]
        if not visited[currentNode]:

     return connected_components

def dfs(grath, v, visited, component):
    visited[v] = True
    component.append(v)
    for i in grath[v]:
        if not visited[i]:
            dfs(grath, i, visited, component)
