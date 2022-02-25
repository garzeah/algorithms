# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    global_maximum_sum = float('-inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.find_maximum_path_sum_recursive(root)
        return self.global_maximum_sum

    def find_maximum_path_sum_recursive(self, curr_node):
        if curr_node is None:
            return 0

        max_path_sum_from_left = self.find_maximum_path_sum_recursive(
          curr_node.left)
        max_path_sum_from_right = self.find_maximum_path_sum_recursive(
          curr_node.right)

        # Ignore paths with negative sums, since we need to find the maximum
        # sum we should ignore any path which has an overall negative sum.
        max_path_sum_from_left = max(max_path_sum_from_left, 0)
        max_path_sum_from_right = max(max_path_sum_from_right, 0)

        # Maximum path sum at the current node will be equal to the sum from the
        # left subtree + the sum from right subtree + val of current node
        local_maximum_sum = max_path_sum_from_left + max_path_sum_from_right + curr_node.val

        # Update the global maximum sum
        self.global_maximum_sum = max(self.global_maximum_sum, local_maximum_sum)

        # Maximum sum of any path from the current node will be equal to the maximum of
        # the sums from left or right subtrees plus the value of the current node
        return max(max_path_sum_from_left, max_path_sum_from_right) + curr_node.val

# Time Complexity: The time complexity of the above algorithm is O(N), where ‘N’
# is the total number of nodes in the tree. This is due to the fact that
# we traverse each node once.

# Space Complexity: The space complexity of the above algorithm will be O(N) in
# the worst case. This space will be used to store the recursion stack. The
# worst case will happen when the given tree is a linked
# list (i.e., every node has only one child).