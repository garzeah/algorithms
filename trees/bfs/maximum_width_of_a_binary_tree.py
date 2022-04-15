# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue = deque([[root, 1]])
        max_width = 0

        while queue:
            # Getting the indexes for the first and last child in the current level
            left, right = queue[0][1], queue[-1][1]
            # Formula for calculating the width using indexes
            max_width = max(max_width, right - left + 1)

            for _ in range(len(queue)):
                curr_node, index = queue.popleft()

                # Adding the next levels while calculating their indexes
                if curr_node.left:
                    queue.append([curr_node.left, index * 2])

                if curr_node.right:
                    queue.append([curr_node.right, index * 2 + 1])

        return max_width

# Time Complexity: O(n) where n is the number of nodes
# Space Complexity: O(w) where w is the biggest number of nodes in a level