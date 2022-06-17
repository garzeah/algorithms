# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)

    def dfs(self, curr, max_val):
        if curr is None:
            return 0

        # Only a good node if the current value is
        # greater than or equal to the current max
        # as we traverse along the path
        if curr.val >= max_val:
            res = 1

        left = self.dfs(curr.left, max(curr.val, max_val))
        right = self.dfs(curr.right, max(curr.val, max_val))

        return res + left + right

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solution: https://www.youtube.com/watch?v=7cp5imvDzl4
