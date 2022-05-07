class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {}

        # Building out our adjaceny list
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        queue, visited, count = deque(), set(), 0

        for vertex in range(n):
            if vertex in visited:
                continue

            queue.append(vertex)

            # Using BFS to visit each node
            while queue:
                curr = queue.popleft()

                if curr in visited:
                    continue

                visited.add(curr)

                for node in adj_list[curr]:
                    queue.append(node)

            count += 1
        return count

# Time complexity: O(V + E) because we are traversing
# each node once.

# Space Complexity: O(V + E) to build out the adjaceny list.

# Solution: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/discuss/400707/Simple-DFS-and-BFS-Python-solutions-using-a-dictionary