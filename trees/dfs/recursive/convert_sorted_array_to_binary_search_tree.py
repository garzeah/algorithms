# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.build_tree(nums, 0, len(nums) - 1)

    def build_tree(self, nums, start, end):
        if start <= end:
            mid = (start + end) // 2

            root = TreeNode(nums[mid])
            root.left = self.build_tree(nums, start, mid - 1)
            root.right = self.build_tree(nums, mid + 1, end)

            return root

# Time Complexity: O(n) because we visit each index once.
# Space Complexity: O(n) because we the stack space when doing recursion.
# Solution: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/discuss/605644/Easy-to-Understand-or-Faster-than-98-or-Recursive-or-Simple-or-Python-Solution
