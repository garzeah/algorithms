class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 0:
            return []

        # With only one node, since its in-degrees will
        # be 0, therefore, we need to handle it separately
        if n == 1:
            return [0]

        # a. Initialize the graph
        inDegree, adj = {}, {}
        for i in range(n):
            inDegree[i] = 0 # Count of incoming edges
            adj[i] = [] # Adjacency list graph

        # b. Build the graph. We are getting every possible
        # combination of trees we can possibly make
        for (n1, n2) in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

            inDegree[n1] += 1
            inDegree[n2] += 1

        # c. Find all leaves (all nodes with 1 in-degrees)
        # since we plan on removing leaves level by level
        leaves = deque()
        for key in inDegree:
            if inDegree[key] == 1:
                leaves.append(key)

        # d. Want to remove leaves level by level and once we're
        # at the last level, we'll see which nodes are remaining
        # giving us the minimum height tree(s)
        layer = []
        while leaves:
            layer = [] # Clear the array for each level

            # Multi-source since we want to clear by level
            for _ in range(len(leaves)):
                leaf = leaves.popleft()
                layer.append(leaf)

                # Finding all leaves so we can repeat
                for nei in adj[leaf]:
                    inDegree[nei] -= 1
                    if inDegree[nei] == 1:
                        leaves.append(nei)

        return layer

# Time Complexity: In step ‘d’, each node can become a source only once and
# each edge will be accessed and removed once. Therefore, the time
# complexity of the above algorithm will be O(V+E), where ‘V’ is
# the total nodes and ‘E’ is the total number of the edges.

# Space Complexity: The space complexity will be O(V+E), since we are
# storing all of the edges for each node in an adjacency list.

# Explanation: https://leetcode.com/problems/minimum-height-trees/discuss/952374/Python-3-approaches-Detailed-Explanation-and-Visuals