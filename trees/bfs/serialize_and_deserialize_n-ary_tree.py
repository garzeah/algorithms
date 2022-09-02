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
        if root is None:
            return root

        res, queue = [], [root]

        # For each node, we want to append the value and unpack the children
        for node in queue:
            if node:
                res.append(str(node.val))
                queue += None, *node.children # Can use the asterisk to unpack children
            else:
                res.append("null")

        return ",".join(res)


    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if data is None:
            return data

        if len(data) == 0:
            return data

        # Assigning pos. to 2 because we'll be starting at the 2nd node
        nodes, queue, pos = data.split(","), deque(), 2
        root = Node(int(nodes[0]), []) # Creating our first node and its children
        queue.append(root)

        while queue:
            node = queue.popleft()

            # Since each group of children is separated by a null,
            # we want to append the node's corresponding children
            while pos < len(nodes) and nodes[pos] != "null":
                node.children.append(Node(int(nodes[pos]), []))
                pos += 1

            pos += 1 # Since children are separated by a null, move it up
            queue += node.children # Adding the next level of children

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

# Solution: https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/discuss/1976476/Short-Python-Iterative-BFS-Solution