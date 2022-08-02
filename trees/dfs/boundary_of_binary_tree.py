# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        # Checks for a leaf
        def isLeaf(node):
            if node.left is None and node.right is None:
                return True

            return False

        # Finds every left boundary of a tree as long as it's not a leaf
        def findLeftBoundary(node):
            left = []

            while node and isLeaf(node) is False:
                left.append(node.val)

                if node.left:
                    node = node.left
                else:
                    node = node.right

            return left

        # Finds every right boundary of a tree as long as it's not a leaf
        def findRightBoundary(node):
            right = []

            while node and isLeaf(node) is False:
                right.append(node.val)

                if node.right:
                    node = node.right
                else:
                    node = node.left

            return right

        # Finds leaves
        def findLeaves(node, leaves = []):
            if isLeaf(node):
                leaves.append(node.val)
            if node.left:
                findLeaves(node.left, leaves)
            if node.right:
                findLeaves(node.right, leaves)

            return leaves

        if root is None:
            return []

        if isLeaf(root):
            return [root.val]

        left = findLeftBoundary(root.left) # Finds every left boundary that's not a leaf
        right = findRightBoundary(root.right) # Finds every right boundary that's not a leaf
        leaves = findLeaves(root) # Finds leaves
        res = [root.val]

        return res + left + leaves + right[::-1]

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solution: https://leetcode.com/problems/boundary-of-binary-tree/discuss/1219771/Python-Explained-and-Visualized