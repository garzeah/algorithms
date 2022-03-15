# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # While we still have sub-arrays
        if inorder:
            # Getting the index of the first value of preorder in inorder
            # since it is the root. As preoreder shrinks, we can use each value
            # we pop to find the left and right subtrees when we search for the
            # index of it in inorder since everything to the left belongs on
            # the left sub-tree and everything on the right belongs to the right sub-tree
            mid = inorder.index(preorder.pop(0))

            # Root will always be the index of the first
            root = TreeNode(inorder[mid])

            root.left = self.buildTree(preorder, inorder[0:mid])
            root.right = self.buildTree(preorder, inorder[mid + 1:])
            return root

# Time Complexity: O(n^2) because we are searching for the index and the recursion is O(n). We can optimize this using deque and popping left. This
# would happen in the event our tree is a linked list.

# Space Complexity: O(n^2) space in the event it is a linked list?