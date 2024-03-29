# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[0]

    # Want to check if each subtree is balanced
    def dfs(self, curr):
        # Want to return 2 values, whether it's balanced and the height
        if curr is None:
            return [True, 0]

        left, right = self.dfs(curr.left), self.dfs(curr.right)
        # Checking if each subtree is balanced
        is_balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

        return [is_balanced, 1 + max(left[1], right[1])]

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solution: https://www.youtube.com/watch?v=QfJsau0ItOY