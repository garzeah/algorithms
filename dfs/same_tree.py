# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Path ended at the same node
        if p is None and q is None:
            return True

        # Path did not end at the same node
        if p is None or q is None:
            return False

        # Doesn't have the same values
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Time Complexity: O(n)
# Space Complexity: O(n)