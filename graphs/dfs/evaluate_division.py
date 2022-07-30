class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Initialize Graph
        adj = {} # numerator: { denominator: value }

        # Build out adj. list and corresponding relationships
        for i, (num, den) in enumerate(equations):
            # numerator / denominator = values[i]
            if num not in adj:
                adj[num] = {}
            adj[num][den] = values[i]

            # denominator / numerator= 1 / values[i]
            if den not in adj:
                adj[den] = {}
            adj[den][num] = 1 / values[i] # Reciprocal

        res = []
        for query in queries:
            res.append(self.dfs(adj, set(), query[0], query[1]))
        return res

    # Step 2. DFS function
    def dfs(self, adj, visited, num, den):
        # Neither the num. or den. exists
        if num not in adj or den not in adj:
            return -1.0

        # We have performed this calculation already
        if den in adj[num]:
            return adj[num][den]

        # Numerator may be connected to denominator through neighbors use
        # dfs to see if there is a path from numerator to denominator
        for nei in adj[num]:
            if nei not in visited:
                visited.add(nei)
                temp = self.dfs(adj, visited, nei, den)
                if temp == -1:
                    continue
                else:
                    return adj[num][nei] * temp
        return -1

# Time Complexity: O(n * m) where n is the number of equations and m
# is the number of queries.

# Space Complexity: O(n) where n is the number of equations.

# Solution: https://www.youtube.com/watch?v=EfkvVigVou0