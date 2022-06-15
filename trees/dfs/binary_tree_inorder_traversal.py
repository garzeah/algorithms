# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.dfs(res, root)
        return res

    def dfs(self, res, curr):
        if curr is None:
            return

        self.dfs(res, curr.left)
        res.append(curr.val)
        self.dfs(res, curr.right)

# Time Complexity: O(n)
# Space Complexity: O(n)
