class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        curr_path, res = [0], []
        return self.dfs(graph, 0, curr_path, res)

    # Since it is acyclic, we do not have to worry about keeping track
    # of previous nodes. We will use end_of_path to keep track when
    # we want to append the current path into our result
    def dfs(self, adj, i, curr_path, res):
        if i == len(adj) - 1:
            res.append(curr_path)
            return

        for nei in adj[i]:
            self.dfs(adj, nei, curr_path + [nei], res)

        return res

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solution: https://www.youtube.com/watch?v=xM8uxH0vcRw