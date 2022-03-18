# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.global_max_sum = float('-inf')
        self.dfs(root)
        return self.global_max_sum

    def dfs(self, curr_node):
        if curr_node is None:
            return 0

        max_path_sum_from_left = self.dfs(curr_node.left)
        max_path_sum_from_right = self.dfs(curr_node.right)

        # Ignore paths with negative sums, since we need to find the maximum sum we should
        # ignore any path which has an overall negative sum.
        max_path_sum_from_left = max(max_path_sum_from_left, 0)
        max_path_sum_from_right = max(max_path_sum_from_right, 0)

        # Maximum path sum at the current node will be equal to the sum from the left subtree +
        # the sum from right subtree + val of current node
        local_max_sum = max_path_sum_from_left +  max_path_sum_from_right + curr_node.val

        # Update the global maximum sum
        self.global_max_sum = max(self.global_max_sum, local_max_sum)

        # Maximum sum of any path from the current node will be equal to the maximum of
        # the sums from left or right subtrees plus the value of the current node
        return max(max_path_sum_from_left,  max_path_sum_from_right) + curr_node.val

# Time Complexity: O(n)
# Space Complexity: O(n)