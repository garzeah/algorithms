# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first, self.second, self.prev = None, None, None
        self.dfs(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    # Want to perform inorder traversal so we can compare the child
    # with the parent to see if any nodes are violating a BST
    def dfs(self, root):
        if root is None:
            return

        self.dfs(root.left)

        # Recording a previous and whenever we find a child
        # that is greater than its parent, we must record
        # which nodes we want to swap
        if self.prev:
            if self.prev.val > root.val:
                if self.first is None:
                    self.first = self.prev
                self.second = root
        self.prev = root

        self.dfs(root.right)

# Time Complexity: O(n)
# Space Complexity:O(n)
# Solution: https://leetcode.com/problems/recover-binary-search-tree/discuss/671363/On-paper-explanantionWell-commented-easy-understand