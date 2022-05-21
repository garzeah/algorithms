# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        curr_path, all_paths = [], []
        self.find_paths_recursive(root, targetSum, curr_path, all_paths)
        return all_paths


    def find_paths_recursive(self, curr_node, targetSum, curr_path, all_paths):
        if curr_node is None:
            return

        # Add the current node to the path
        curr_path.append(curr_node.val)

        # If the current node is a leaf and its value is equal to targetSum, save the current path
        if curr_node.val == targetSum and curr_node.left is None and curr_node.right is None:
            all_paths.append(list(curr_path))
        else:
        # Traverse the left sub-tree
            self.find_paths_recursive(curr_node.left, targetSum - curr_node.val, curr_path, all_paths)
        # Traverse the right sub-tree
            self.find_paths_recursive(curr_node.right, targetSum - curr_node.val, curr_path, all_paths)

        # Remove the current node from the path to backtrack, we need to remove the current node
        # while we are going up the recursive call stack.
        del curr_path[-1]

# Time Complexity: The time complexity of the above algorithm is O(N^2), where ‘N’ is the
# total number of nodes in the tree. This is due to the fact that we traverse each node
# once (which will take O(N)), and for every leaf node, we might have to store its path
# (by making a copy of the current path) which will take O(N).

# Space Complexity: O(N*logN), refer to Grokking it's complex