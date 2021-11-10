def breath_first_search(graph, source):
    queue = [source]
    while len(queue) > 0:
        node = queue.pop()
        print(node)
        for neighbor in graph[node]:
            queue.insert(0, neighbor)


graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

breath_first_search(graph, 'a')
