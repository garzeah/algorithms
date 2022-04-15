# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = deque()
        if root is None:
            return result

        queue = deque([root])

        while queue:
            curr_level = []

            for _ in range(len(queue)):
                curr_node = queue.popleft()

                # Add the node to the current level
                curr_level.append(curr_node.val)

                # Insert the children of current node in the queue
                if curr_node.right:
                    queue.append(curr_node.right)

            result.appendleft(curr_level)

        return result

# Time Complexity: O(n)
# Space Complexity: O(n)