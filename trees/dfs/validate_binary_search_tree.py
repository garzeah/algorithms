# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        self.dfs(root, res)

        # Validating whether it's a BST or not
        for i in range(1, len(res)):
            if res[i - 1] >= res[i]:
                return False

        return True


    def dfs(self, curr_node, res):
        if curr_node is None:
            return

        # Doing in-order traversal creates a BST
        # assuming the numbers are valid
        self.dfs(curr_node.left, res)
        res.append(curr_node.val)
        self.dfs(curr_node.right, res)

# Time Complexity: O(n)
# Space Complexity: O(n)