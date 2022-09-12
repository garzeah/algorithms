# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # Want to get the sums of each sub-tree
        sums = []
        self.dfs(root, sums)

        # We can get the max product of two subtrees by multiplying the
        # subtree_sum with (total_sum - subtree_sum) since if we are
        # multiplying a sum with the remainder of the sub-tree
        total_sum, res = sums[-1], 0
        for subtree_sum in sums:
            curr = subtree_sum * (total_sum - subtree_sum)
            res = max(res, curr)

        return res % (10**9 + 7)

    def dfs(self, root, sums):
        if root is None:
            return 0

        left_sum = self.dfs(root.left, sums)
        right_sum = self.dfs(root.right, sums)

        subtree_sum = left_sum + right_sum + root.val
        sums.append(subtree_sum)

        return subtree_sum

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solution: https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/discuss/1413108/Python-Explained-Solution-with-Diagrams-oror-Beats-99