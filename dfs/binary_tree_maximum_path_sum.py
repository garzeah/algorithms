# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.global_max = float('-inf')
        self.dfs(root)
        return self.global_max

    def dfs(self, curr_node):
        if curr_node is None:
            return 0

        max_left = self.dfs(curr_node.left)
        max_right = self.dfs(curr_node.right)

        # Ignore paths with negative sums, since we need to find the maximum sum we should
        # ignore any path which has an overall negative sum.
        max_left = max(max_left, 0)
        max_right = max(max_right, 0)

        # Maximum path sum at the current node will be equal to the sum from the left subtree +
        # the sum from right subtree + val of current node
        local_max = curr_node.val + max_left +  max_right

        # Update the global maximum sum
        self.global_max = max(self.global_max, local_max)

        # Maximum sum of any path from the current node will be equal to the maximum of
        # the sums from left or right subtrees plus the value of the current node
        return curr_node.val + max(max_left,  max_right)

# Time Complexity: O(n)
# Space Complexity: O(n)