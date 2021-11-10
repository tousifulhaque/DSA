def depth_first_search(graph, source):

    stack = [source];

    while len(stack) > 0 :
        current = stack.pop()
        print(current)
        for neighbor in graph[current]:
            stack.append(neighbor)
            print(stack)


graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

depth_first_search(graph, 'a')