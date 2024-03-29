class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree, adj, sorted_order = {}, {}, []
        if numCourses <= 0:
            return sorted_order

        # a. Initializing incoming degrees and adjancey list
        for i in range(numCourses):
            in_degree[i] = 0 # Count of incoming prerequisites
            adj[i] = [] # Adjacency list

        # b. Build the adj
        for child, parent in prerequisites:
            adj[parent].append(child)  # Put the child into it's parent's list
            in_degree[child] += 1  # Increment child's in_degree

        # c. Find all sources i.e., all numCourses with 0 in-degrees
        sources = deque()
        for key in in_degree:
            if in_degree[key] == 0:
                sources.append(key)

        # d. For each source, add it to the sorted_order and subtract
        # one from all of its children's in-degrees if a child's
        # in-degree becomes zero, add it to the sources queue
        while sources:
            vertex = sources.popleft()
            sorted_order.append(vertex)

            # Want to decrement the incoming degrees
            # in a vertex to get the sorted order
            for child in adj[vertex]:
                in_degree[child] -= 1
                # When a vertex has 0 in-degrees, it becomes
                # a source so add it into our queue
                if in_degree[child] == 0:
                    sources.append(child)

        # Topological sort is not possible as the graph has a cycle
        if len(sorted_order) != numCourses:
            return []

        return sorted_order

# Time Complexity: In step ‘d’, each vertex will become a source only
# once and each edge will be accessed and removed once. Therefore,
# the time complexity of the above algorithm will be O(V+E),
# where ‘V’ is the total number of numCourses and ‘E’ is the
# total number of prerequisites in the graph.

# Space Complexity: The space complexity will be O(V+E), since we
# are storing all of the prerequisites for each vertex in an adjacency list.
