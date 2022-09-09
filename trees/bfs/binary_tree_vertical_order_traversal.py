# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return root

        cols = defaultdict(list) # { column index : [vertical values] }
        queue = deque([(root, 0)]) # Pair of node and column index

        # As we perform a BFS search, we want to keep track of the
        # column indexes so everytime we find a left/right node
        # we will subtract/add the column index with 1
        while queue:
            node, col_idx = queue.popleft()

            cols[col_idx].append(node.val)

            if node.left:
                queue.append((node.left, col_idx - 1))

            if node.right:
                queue.append((node.right, col_idx + 1))

        # Get a list of sorted keys so we can get the values in vertical order traversal
        res = []
        for key in sorted(cols.keys()):
            res.append(cols[key])

        return res

# Time Complexity: O(nlogn) bc of sorting where n is the amount of columns
# Space Complexity: O(n)
# Solution: https://leetcode.com/problems/binary-tree-vertical-order-traversal/discuss/2088921/Easiest-solution-to-understand.-Faster-than-95.-Python
