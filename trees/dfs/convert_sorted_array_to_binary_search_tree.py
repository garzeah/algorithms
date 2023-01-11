# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if nums:
            start, end = 0, len(nums)
            mid = (start + end) // 2

            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums[start:mid])
            root.right = self.sortedArrayToBST(nums[mid + 1:])

            return root

# Time Complexity: O(n) because we visit each index once.
# Space Complexity: O(n) because we the stack space when doing recursion.
# Solution: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/discuss/605644/Easy-to-Understand-or-Faster-than-98-or-Recursive-or-Simple-or-Python-Solution
