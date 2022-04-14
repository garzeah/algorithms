# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is None:
            return result

        queue = deque()
        queue.append(root)

        while queue:
            levelSize = len(queue)

            for i in range(levelSize):
                curr_node = queue.popleft()

                # If it is the last node of this level, add it to the result
                if i == levelSize - 1:
                    result.append(curr_node.val)

                # Insert the children of current node in the queue
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

        return result

# Time Complexity: O(n)
# Space Complexity: O(n)