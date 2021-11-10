def dfs_wrecursion(graph, source):
    print(source)
    for neighbor in graph[source]:
        dfs_wrecursion(graph, neighbor)


graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

dfs_wrecursion(graph, 'a')