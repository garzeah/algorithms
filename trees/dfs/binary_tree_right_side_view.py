# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return self.dfs(root, 0, [])

    def dfs(self, root, height, res):
        if root is None:
            return

        if height == len(res):
            res.append(root.val)

        self.dfs(root.right, height + 1, res)
        self.dfs(root.left, height + 1, res)

        return res
# Time Complexity: O(n)
# Space Complexity: O(n) bc of recursion stack