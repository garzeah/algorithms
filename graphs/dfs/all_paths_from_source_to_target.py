class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        curr_path, res = [], []
        end_of_path = len(graph) - 1
        return self.dfs(graph, 0, end_of_path, [0], res)

    # Since it is acyclic, we do not have to worry about keeping track
    # of previous nodes. We will use end_of_path to keep track when
    # we want to append the current path into our result
    def dfs(self, graph, node, end_of_path, curr_path, res):
        if node == end_of_path:
            res.append(curr_path)

        for nei in graph[node]:
            self.dfs(graph, nei, end_of_path, curr_path + [nei], res)

        return res

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solution: https://www.youtube.com/watch?v=xM8uxH0vcRw