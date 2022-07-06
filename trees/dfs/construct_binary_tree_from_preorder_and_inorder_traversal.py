# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        queue = deque()
        for num in preorder:
            queue.append(num)

        return self.buildTreeHelper(queue, inorder)

    def buildTreeHelper(self, preorder, inorder):
        if inorder:
            # Want to pop the first value of preorder and use that with inorder
            # to build a tree since all the values of the left and right of the
            # popped value can be use to build both sides of the tree
            preorder_num = preorder.popleft()
            mid = inorder.index(preorder_num)

            root = TreeNode(inorder[mid])
            root.left = self.buildTreeHelper(preorder, inorder[:mid]) # Want all values left of mid
            root.right = self.buildTreeHelper(preorder, inorder[mid + 1:]) # Want all values right of mid

            return root

# Time Complexity: O(n) because of the recursion stack.

# Space Complexity: O(n) because of recursion stack.