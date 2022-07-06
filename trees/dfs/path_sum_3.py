# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        return self.dfs(root, target, [])

    def dfs(self, root, target, curr_path):
        if root is None:
            return 0

        # Add the current node to the path
        curr_path.append(root.val)
        res, path_sum = 0, 0

        # As we added a new node to the current path, we should find
        # the sums of all sub-paths ending at the current node. If
        # the sum of any sub-path is equal to ‘target’ we will
        # increment our path count. Also, if we iterate
        # backwards then we can get the sub-paths.
        for i in range(len(curr_path) - 1, -1, -1):
            path_sum += curr_path[i]
            if path_sum == target:
                res += 1

        # Traverse the left and right sub-trees
        res += self.dfs(root.left, target, curr_path)
        res += self.dfs(root.right, target, curr_path)

        # Remove the current node from the path to backtrack we need to remove
        # the current node while we are going up the recursive call stack
        del curr_path[-1]

        return res

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