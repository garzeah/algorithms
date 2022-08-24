class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Initialize Graph
        adj = defaultdict(dict) # numerator: { denominator: value }

        # Build out adj. list and corresponding relationships
        for i, (num, den) in enumerate(equations):
            # numerator / denominator = values[i]
            adj[num][den] = values[i]
            # denominator / numerator= 1 / values[i]
            adj[den][num] = 1 / values[i] # Reciprocal

        res = []
        for query in queries:
            res.append(self.dfs(adj, set(), query[0], query[1]))
        return res

    # Step 2. DFS function
    def dfs(self, adj, visited, start, end):
        # Neither the num. or den. exists
        if start not in adj or end not in adj:
            return -1.0

        # We have performed this calculation already
        if end in adj[start]:
            return adj[start][end]

        # Numerator may be connected to denominator through neighbors use
        # dfs to see if there is a path from numerator to denominator
        for nei in adj[start]:
            if nei not in visited:
                visited.add(nei)
                res = self.dfs(adj, visited, nei, end)
                if res == -1.0:
                    continue
                else:
                    return adj[start][nei] * res

        return -1.0

# Time Complexity: O(n * m) where n is the number of equations and m
# is the number of queries.

# Space Complexity: O(n) where n is the number of equations.

# Solution: https://www.youtube.com/watch?v=EfkvVigVou0