# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        results = []
        self.find_right_side(root, results, 0)
        return results

    def find_right_side(self, curr_node, results, depth):
        if curr_node:
            if depth == len(results):
                results.append(curr_node.val)

            self.find_right_side(curr_node.right, results, depth + 1)
            self.find_right_side(curr_node.left, results, depth + 1)

# Time Complexity: O(n)
# Space Complexity: O(n) bc of recursion stack