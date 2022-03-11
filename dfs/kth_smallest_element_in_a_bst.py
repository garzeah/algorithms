# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k # Use as internal counter.
        return self.dfs(root, None)

    def dfs(self, curr_node, ans):
        if curr_node is None or ans: # Stop early.
            return ans

        # DFS in-order traversal
        ans = self.dfs(curr_node.left, ans)
        self.k -= 1 # Decrement the counter until k is 0

        if self.k == 0:
            return curr_node.val # Set ans to node value.

        ans = self.dfs(curr_node.right, ans)

        return ans

# Time Complexity: O(n)
# Space Complexity: O(n) (worst case in the event it's a linked list)