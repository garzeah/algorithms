class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Added 1 so we can start counting from 1 instead of 0 for simplicity
        parents = [i for i in range(len(edges) + 1)] # Parent at each vertex
        ranks = [1] * (len(edges) + 1) # Size of the graph at each vertex

        # Starting
        # [0, 1, 2, 3]
        # [1, 1, 1, 1]

        # [1, 2]
        # [0, 1, 1, 3]
        # [1, 3, 1, 1]

        # [1, 3]
        # [0, 1, 1, 1]
        # [1, 3, 1, 1]

        # [2, 3]
        # root_x and root_y would equal each other
        # meaning we found our redundant connection

        # Want to find the parent of a node
        def find(vertex):
            p = parents[vertex]

            while p != parents[p]:
                parents[p] = parents[parents[p]]
                p = parents[p] # Moving pointer up

            return p

        def union(x, y):
            # Want to find the parents of both edges
            root_x, root_y = find(x), find(y)

            # If they have the same parent, we have found our
            # redundant connection since if we merged it, we
            # would have a cycle and not a valid tree
            if root_x == root_y:
                return False

            # Else if rank of root_x is >= rank of root_y
            elif ranks[root_x] >= ranks[root_y]:
                parents[root_y] = root_x # root_x is now parent of root_y
                ranks[root_x] += ranks[root_y] # Increase the rank (size) of root_x

            # Else rank of root_x is < rank of root_y
            else:
                parents[root_x] = root_y # root_y is now parent of root_x
                ranks[root_y] += ranks[root_x] # Increase the rank (size) of root_y

            return True

        for (n1, n2) in edges:
            if union(n1, n2) is False:
                return [n1, n2]

# TC: O(n) where n is the length of endges
# SC: O(n)