# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        output = []
        self.inorder(root, output)

        for i, node in enumerate(output):
            if node == p:
                if i == len(output) - 1: # At the end...
                    return None
                else:
                    return output[i + 1]

    def inorder(self, curr_node, output):
        if curr_node is None:
            return

        self.inorder(curr_node.left, output)
        output.append(curr_node)
        self.inorder(curr_node.right, output)

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solution: https://leetcode.com/problems/inorder-successor-in-bst/discuss/72730/Python-iterative-and-recursive-solutions-with-comments-(O(n)-and-O(k)-time).