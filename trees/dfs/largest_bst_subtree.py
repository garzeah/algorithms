# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if root is None:
            # When we hit our base case we want to keep track of...
            # 1) Is it a bst?
            # 2) Is the left child < root
            # 3) Is the right child > root
            # 4) Size of the sub-tree
            # Want to keep track of min and max so we can use the left_max and right_min
            # to determine whether the subtree is a valid BST at our current root. We
            # will also use the left_min and right_max to calculate to calculate the
            # the values we need when comparing the root to left_max and right_min
            return [True, float('inf'), float('-inf'), 0]

        left_is_bst, left_min, left_max, left_size = self.dfs(root.left)
        right_is_bst, right_min, right_max, right_size = self.dfs(root.right)

        # If we have a binary search tree...
        if (left_is_bst and right_is_bst and root.val > left_max and root.val < right_min):
            # When we hit our base case, we want to handle
            # the infinite values and calc. max subtree
            left_min = root.val if left_min == float('inf') else left_min
            right_max = root.val if right_max == float('-inf') else right_max
            local_res = left_size + right_size + 1
            self.res = max(self.res, local_res)

            return [True, left_min, right_max, left_size + right_size + 1]
        else:
            # Return false, +- inf for comparison and size of 0 since it's not a BST
            return [False, float('inf'), float('-inf'), 0]

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solution: https://www.youtube.com/watch?v=t3kHAoRT5iQ