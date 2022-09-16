# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        successor = None

        # We can traverse through each node in ascending order iteratively
        # and as soon we find a root that is greater than p, we have
        # found our successor
        while root:
            if root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right

        return successor

# Time Complexity: O(h) where h is the height of the tree
# Space Complexity: O(1)
# Solution: https://leetcode.com/problems/inorder-successor-in-bst/discuss/72656/JavaPython-solution-O(h)-time-and-O(1)-space-iterative

