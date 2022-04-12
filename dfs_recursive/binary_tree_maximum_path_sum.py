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

        left_max = self.dfs(curr_node.left)
        right_max = self.dfs(curr_node.right)

        # Ignore paths with negative sums, since we need to find the maximum
        # sum we should ignore any path which has an overall negative sum.
        left_max = max(left_max, 0)
        right_max = max(right_max, 0)

        # Maximum path sum at the current node will be equal to the sum of
        # the value of the current node and the sums of the left and right subtree
        local_max = curr_node.val + left_max + right_max

        # Update the global maximum sum
        self.global_max = max(self.global_max, local_max)

        # Maximum sum of any path from the current node will be equal to the value
        # of the current node and the maximum of the sums from left or right subtrees
        return curr_node.val + max(left_max, right_max)

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solution: https://www.youtube.com/watch?v=Hr5cWUld4vU