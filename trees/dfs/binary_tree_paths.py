# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        self.dfs(root, "", res)
        return res

    def dfs(self, root, curr_path, res):
        if root is None:
            return

        if root.left is None and root.right is None:
            curr_path += str(root.val)
            res.append(curr_path)

        curr_path += str(root.val) + "->"

        self.dfs(root.left, curr_path, res)
        self.dfs(root.right, curr_path, res)