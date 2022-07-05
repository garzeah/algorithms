"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_copy = { None: None } # Map of old node to copied node

        curr = head
        while curr: # 1st pass we will build out our hash map
            old_to_copy[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr: # 2nd pass we will build out pointers
            copy = old_to_copy[curr]
            copy.next = old_to_copy[curr.next]
            copy.random = old_to_copy[curr.random] # Works bc we already built out the existing nodes in 1st pass
            curr = curr.next

        return old_to_copy[head]

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solution: https://www.youtube.com/watch?v=5Y2EiZST97Y