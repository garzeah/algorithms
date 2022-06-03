# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def treeToGraph(self, root):
        queue = deque([root])
        adj = {}

        while queue:
            curr = queue.popleft()

            # Initialize adj. list for each node
            if curr not in adj:
                adj[curr] = []

            # Since it is an undirected graph, we'll be adding connections             # to both parent and child as well as creating a list for the               # child node if none exists then lastly add it to our queue
            if curr.left:
                adj[curr].append(curr.left)

                if curr.left not in adj:
                    adj[curr.left] = []

                adj[curr.left].append(curr)
                queue.append(curr.left)

            if curr.right:
                adj[curr].append(curr.right)

                if curr.right not in adj:
                    adj[curr.right] = []

                adj[curr.right].append(curr)
                queue.append(curr.right)

        return adj


    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if root is None or target is None:
            return []

        # Using BFS to build an adjacency list from our tree
        adj = self.treeToGraph(root)

        queue = deque([(target, 0)])
        visited = set()
        output = []

        # Performing BFS on our queue to get k distance from target
        while queue:
            curr, distance = queue.popleft()

            if curr in visited:
                continue

            visited.add(curr)

            for nei in adj[curr]:
                queue.append((nei, distance + 1))

            if distance == k:
                output.append(curr.val)

        return output

# Time Complexity: O(V + E) because for every vertex we visit its neighbors.

# Space Complexity: O(V + E) to store the adjanceny list.

# Solution: https://www.youtube.com/watch?v=3sv9yF1xecQ