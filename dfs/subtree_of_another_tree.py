# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        if subRoot is None:
            return True

        return self.dfs(root, subRoot)

    def dfs(self, root, subRoot):
        if root is None:
            return False

        if root.val == subRoot.val and self.checkTree(root, subRoot):
            return True

        return self.dfs(root.left, subRoot) or self.dfs(root.right, subRoot)

    def checkTree(self, root1, root2):
        if root1 is None and root2 is None:
            return True

        if root1 is None or root2 is None:
            return False

        if root1.val != root2.val:
            return False

        return self.checkTree(root1.left, root2.left) and self.checkTree(root1.right, root2.right)

# Time Complexity: O(n*m) where n is the amount of nodes we traverse in dfs and m is the
# amount of nodes we traverse when checking a tree

# Space Complexity: O(n)
