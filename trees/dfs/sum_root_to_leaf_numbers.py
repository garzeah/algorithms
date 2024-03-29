# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.find_sums(root, 0)

    def find_sums(self, root, path_sum):
        if root is None:
            return 0

        # Calculate the path number of the current node
        path_sum = 10 * path_sum + root.val

        # If the current node is a leaf, return the current path sum
        if root.left is None and root.right is None:
            return path_sum

        # Traverse the left and the right sub-tree
        return self.find_sums(root.left, path_sum) + self.find_sums(root.right, path_sum)

# Time Complexity: The time complexity of the above algorithm is O(N),
# where ‘N’ is the total number of nodes in the tree. This is due to
# the fact that we traverse each node once.

# Space Complexity: The space complexity of the above algorithm will
# be O(N) in the worst case. This space will be used to store the
# recursion stack. The worst case will happen when the given tree
# is a linked list (i.e., every node has only one child).
