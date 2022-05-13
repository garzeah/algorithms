class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 0:
            return []

        # with only one node, since its in-degrees will be 0, therefore, we need to handle it separately
        if n == 1:
            return [0]

        # a. Initialize the graph
        in_degree = {i: 0 for i in range(n)}  # count of incoming edges
        adj = {i: [] for i in range(n)}  # adjacency list graph

        # b. Build the graph
        for edge in edges:
            n1, n2 = edge[0], edge[1]
            # since this is an undirected graph, therefore, add a link for both the nodes
            adj[n1].append(n2)
            adj[n2].append(n1)
            # increment the in-degrees of both the nodes
            in_degree[n1] += 1
            in_degree[n2] += 1

        # c. Find all leaves i.e., all nodes with 1 in-degrees
        leaves = deque()
        for key in in_degree:
            if in_degree[key] == 1:
                leaves.append(key)

        # d. Remove leaves level by level and subtract each leave's children's in-degrees.
        # Repeat this until we are left with 1 or 2 nodes, which will be our answer.
        # Any node that has already been a leaf cannot be the root of a minimum height tree, because
        # its adjacent non-leaf node will always be a better candidate.
        total_nodes = n
        while total_nodes > 2:
            leaves_size = len(leaves)
            total_nodes -= leaves_size
            for i in range(leaves_size):
                vertex = leaves.popleft()
                # get the node's children to decrement their in-degrees
                for child in adj[vertex]:
                    in_degree[child] -= 1
                    if in_degree[child] == 1:
                        leaves.append(child)

        return list(leaves)

# Time Complexity: In step ‘d’, each node can become a source only once and
# each edge will be accessed and removed once. Therefore, the time
# complexity of the above algorithm will be O(V+E), where ‘V’ is
# the total nodes and ‘E’ is the total number of the edges.

# Space Complexity: The space complexity will be O(V+E), since we are
# storing all of the edges for each node in an adjacency list.

# Explanation: https://www.youtube.com/watch?v=ZfzVig8UqBQ