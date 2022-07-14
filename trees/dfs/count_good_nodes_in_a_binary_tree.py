# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)

    def dfs(self, root, max_val):
        if root is None:
            return 0

        # Only a good node if the current value is
        # greater than or equal to the current max
        # as we traverse along the path
        res = 0
        if root.val >= max_val:
            res += 1

        left = self.dfs(root.left, max(root.val, max_val))
        right = self.dfs(root.right, max(root.val, max_val))

        return res + left + right

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solution: https://www.youtube.com/watch?v=7cp5imvDzl4
