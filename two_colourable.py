def twoColourable(edges: list[list[int]]):
    colours = [False for _ in edges]
    stack = [0]
    node = 0

    while len(stack) > 0:
        node = stack.pop()
        for connection in edges[node]:
            if colours[connection] is None:
                colours[connection] = not colours[node]
                stack.append(connection)
            elif colours[connection] == colours[node]:
                return False

    return True