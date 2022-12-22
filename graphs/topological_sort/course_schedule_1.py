class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree, adj, sortedOrder = {}, {}, []
        if numCourses <= 0:
            return sortedOrder

        # a. Initializing incoming degrees and adjancey list
        for i in range(numCourses):
            inDegree[i] = 0 # Count of incoming prerequisites
            adj[i] = [] # Adjacency list

        # b. Build the adjacency list
        for child, parent in prerequisites:
            adj[parent].append(child)  # Put the child into it's parent's list
            inDegree[child] += 1  # Increment child's inDegree

        # c. Find all sources i.e., all numCourses with 0 in-degrees
        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)

        # d. For each source, add it to the sortedOrder and subtract one from
        # all of its children's in-degrees if a child's in-degree becomes zero,
        # add it to the sources queue
        while sources:
            vertex = sources.popleft()
            sortedOrder.append(vertex)

            # Get the node's children to decrement their in-degrees
            for child in adj[vertex]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)

        # Topological sort is not possible as the graph has a cycle
        if len(sortedOrder) != numCourses:
            return False

        return True

# Time Complexity: In step ‘d’, each vertex will become a source only
# once and each edge will be accessed and removed once. Therefore,
# the time complexity of the above algorithm will be O(V+E),
# where ‘V’ is the total number of numCourses and ‘E’ is the
# total number of prerequisites in the graph.

# Space Complexity: The space complexity will be O(V+E), since we
# are storing all of the prerequisites for each vertex in an adjacency list.
