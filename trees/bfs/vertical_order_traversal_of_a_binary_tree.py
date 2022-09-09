# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return

        pos = defaultdict(list)
        queue = deque([(root, 0, 0)])

        while queue:
            for _ in range(len(queue)):
                curr, row, col = queue.popleft()

                # Want to group together nodes with the same row and column
                pos[(row, col)].append(curr.val)

                if curr.left:
                    queue.append((curr.left, row + 1, col - 1))

                if curr.right:
                    queue.append((curr.right, row + 1, col + 1))


        res = defaultdict(list)
        for (row, col) in sorted(pos.keys(), key=lambda x: x[1]):
            for num in sorted(pos[(row, col)]):
                res[col].append(num)

        return res.values()