"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        res = []
        self.serialize_helper(root, res)
        return ",".join(res)

    def serialize_helper(self, root, res):
        if root is None:
            return ""
        else:
            res.append(str(root.val)) # Get the value
            res.append(str(len(root.children))) # Get the length of its children

            # We want to serialize every child as well
            for child in root.children:
                self.serialize_helper(child, res)

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if len(data) == 0:
            return None
        # Append every value in res to our queue and return them into a tree
        else:
            res, queue = data.split(","), deque()
            [queue.append(res[i]) for i in range(len(res))]
            return self.deserialize_helper(queue)

    def deserialize_helper(self, queue):
        if len(queue) > 0:
            # Retrieving the value and the length of its children
            val, total_children = queue.popleft(), int(queue.popleft())
            root = Node(int(val), []) # Initializing our root

            # For every child a value has, we want to create a root
            # for it and add its children to the base root
            for i in range(total_children):
                root.children.append(self.deserialize_helper(queue))

            return root
        else:
            return None


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

# Solution: https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/discuss/393501/easy-peasy-python-solution-preorder-travel-with-child-count