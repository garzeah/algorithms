# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        # Serializing our results
        def dfs(root):
            if root is None:
                res.append('N')
                return

            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ",".join(res) # Converting to a string


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # Converting string to an array without ','
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == 'N':
                self.i += 1
                return

            node = TreeNode(int(vals[self.i]))
            self.i += 1

            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# TC: O(n)
# SC: O(n)
# Solution: https://www.youtube.com/watch?v=u4JAi2JJhI8