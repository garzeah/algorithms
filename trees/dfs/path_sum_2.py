# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> List[List[int]]:
        res = []
        self.dfs(root, target, [], res)
        return res


    def dfs(self, root, target, curr_path, res):
        if root is None:
            return

        # Add the current node to the path
        curr_path.append(root.val)

        # If the current node is a leaf and its value is equal to target, save the current path
        if root.val == target and root.left is None and root.right is None:
            res.append(list(curr_path))

        # Traverse the left sub-tree
        self.dfs(root.left, target - root.val, curr_path, res)
        # Traverse the right sub-tree
        self.dfs(root.right, target - root.val, curr_path, res)

        # Remove the current node from the path to backtrack, we need to remove the current node
        # while we are going up the recursive call stack.
        del curr_path[-1]

# Time Complexity: The time complexity of the above algorithm is O(N^2), where ‘N’ is the
# total number of nodes in the tree. This is due to the fact that we traverse each node
# once (which will take O(N)), and for every leaf node, we might have to store its path
# (by making a copy of the current path) which will take O(N).

# Space Complexity: O(N*logN), refer to Grokking it's complex