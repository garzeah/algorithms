# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        self.postorder(root, res)
        return res

    def postorder(self, root, res):
        # -1 so that the bottom of the tree is the 0th index
        if root is None:
            return -1

        height = max(
            self.postorder(root.left, res),
            self.postorder(root.right, res)
        ) + 1

        # When height is at 0, we append an empty
        # array so we can append the leaves
        if height >= len(res):
            res.append([])

        res[height].append(root.val)
        return height

# Time Complexity: O(n)
# Space Complexity: O(n)