def topological_sort(vertices, edges):
    in_degree, graph, sorted_order = {}, {}, []
    if vertices <= 0:
        return sorted_order

    # a. Initialize the graph
    for i in range(vertices):
        in_degree[i] = 0 # Count of incoming edges
        graph[i] = [] # Adjacency list graph

    # b. Build the graph
    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)  # Put the child into it's parent's list
        in_degree[child] += 1  # Increment child's in_degree

    # c. Find all sources i.e., all vertices with 0 in-degrees
    sources = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)

    # d. For each source, add it to the sorted_order and subtract one from
    # all of its children's in-degrees if a child's in-degree becomes zero,
    # add it to the sources queue
    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)

        # Get the node's children to decrement their in-degrees
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    # Topological sort is not possible as the graph has a cycle
    if len(sorted_order) != vertices:
        return []

    return sorted_order

# Time Complexity: In step ‘d’, each vertex will become a source only
# once and each edge will be accessed and removed once. Therefore,
# the time complexity of the above algorithm will be O(V+E),
# where ‘V’ is the total number of vertices and ‘E’ is the
# total number of edges in the graph.

# Space Complexity: The space complexity will be O(V+E), since we
# are storing all of the edges for each vertex in an adjacency list.
