# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return self.count_paths_recursive(root, targetSum, [])


    def count_paths_recursive(self, curr_node, targetSum, curr_path):
        if curr_node is None:
            return 0

        # Add the current node to the path
        curr_path.append(curr_node.val)
        path_count, path_sum = 0, 0

        # Find the sums of all sub-paths in the current path list
        for i in range(len(curr_path) - 1, -1, -1):
            path_sum += curr_path[i]
            # If the sum of any sub-path is equal to 'targetSum' we increment our path count.
            if path_sum == targetSum:
                path_count += 1

        # Traverse the left and right sub-trees
        path_count += self.count_paths_recursive(curr_node.left, targetSum, curr_path)
        path_count += self.count_paths_recursive(curr_node.right, targetSum, curr_path)

        # Remove the current node from the path to backtrack we need to remove
        # the current node while we are going up the recursive call stack
        del curr_path[-1]

        return path_count

# Time Complexity: The time complexity of the above algorithm is O(N^2) in the worst case,
# where ‘N’ is the total number of nodes in the tree. This is due to the fact that we
# traverse each node once, but for every node, we iterate the current path. The
# current path, in the worst case, can be O(N) (in the case of a skewed tree).
# But, if the tree is balanced, then the current path will be equal to the
# height of the tree, i.e., O(logN). So the best case of our algorithm
# will be O(NlogN).

# Space Complexity: The space complexity of the above algorithm will be O(N). This
# space will be used to store the recursion stack. The worst case will happen
# when the given tree is a linked list (i.e., every node has only one child).
# We also need O(N) space for storing the currentPath in the worst case.