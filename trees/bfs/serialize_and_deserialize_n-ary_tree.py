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

        result, queue = [], [root]

        for node in queue:
            if node:
                result.append(str(node.val))
                queue += None, *node.children # Can use the asterisk to unpack children
            else:
                result.append("null")

        return ",".join(result)


    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if data is None:
            return data

        if len(data) == 0:
            return data

        nodes, queue, pos = data.split(","), deque(), 2
        root = Node(int(nodes[0]), []) # Creating our first node and its children
        queue.append(root)

        while queue:
            node = queue.popleft()

            # While we aren't at the end we don't have null nodes,
            # we want to append the the node's corresponding children
            while pos < len(nodes) and nodes[pos] != "null":
                node.children.append(Node(int(nodes[pos]), []))
                pos += 1

            pos += 1
            queue += node.children # Adding the next level of children

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

# Solution: https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/discuss/1976476/Short-Python-Iterative-BFS-Solution