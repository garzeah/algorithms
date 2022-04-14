# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        output = []
        self.dfs(root, output)

        # Validating whether it's a BST or not
        for i in range(1, len(output)):
            if output[i - 1] >= output[i]:
                return False

        return True


    def dfs(self, curr_node, output):
        if curr_node is None:
            return

        # Doing in-order traversal creates a BST
        # assuming the numbers are valid
        self.dfs(curr_node.left, output)
        output.append(curr_node.val)
        self.dfs(curr_node.right, output)

# Time Complexity: O(n)
# Space Complexity: O(n)