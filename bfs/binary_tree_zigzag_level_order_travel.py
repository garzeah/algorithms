# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root is None:
            return result

        queue = deque([root])
        left_to_right = True

        while queue:
            curr_level = deque()

            for _ in range(len(queue)):
                curr_node = queue.popleft()

                # Add the node to the current level based on the traverse direction
                if left_to_right:
                    curr_level.append(curr_node.val)
                else:
                    curr_level.appendleft(curr_node.val)

                # Insert the children of current node in the queue
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

            result.append(list(curr_level))

            # Reverse the traversal direction
            left_to_right = not left_to_right

        return result

# Time Complexity: O(n)
# Space Complexity: O(n)