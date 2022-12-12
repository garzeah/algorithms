# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if root is None:
            return 0

        leftMax = self.dfs(root.left)
        rightMax = self.dfs(root.right)

        # Ignore paths with negative sums, since we need to find the maximum
        # sum we should ignore any path which has an overall negative sum
        leftMax = max(leftMax, 0)
        rightMax = max(rightMax, 0)

        # Compute max path sum WITH split
        self.res = max(self.res, root.val + leftMax + rightMax)

        # Return max path sum WITHOUT split
        return root.val + max(leftMax, rightMax)

# TC: O(n)
# SC: O(n)
# Solution: https://www.youtube.com/watch?v=Hr5cWUld4vU

