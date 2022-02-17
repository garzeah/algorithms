# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        if root is None:
            return result

        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue)
            curr_level = 0.0

            for _ in range(level_size):
                curr_node = queue.popleft()

                # Add the node's value to the running sum
                curr_level += curr_node.val

                # Insert the children of current node to the queue
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

            # Append the current level's average to the result array
            result.append(curr_level / level_size)

        return result

# Time Complexity: O(n)
# Space Complexity: O(n)