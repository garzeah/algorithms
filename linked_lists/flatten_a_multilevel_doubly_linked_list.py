"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Traverse the list and look for nodes, where self.child is not None keep the
        # pointer to the previous node and to the original next node merge a child
        # list to the parent list - connect prev and next pointers continue
        # traversing until encountering another node where self.child is
        # not None, or reaching the end of the main list
        curr = head

        while curr:
            # Check for child node
            if curr.child:
                self.merge(curr)

            curr = curr.next

        return head

    def merge(self, curr):
        child = curr.child

        # Traverse child list until we get the last node
        while child.next:
            child = child.next

        # Child is now pointing at the last node of the child list
        # we need to connect child.next to current.next, if there is any
        if curr.next:
            child.next = curr.next
            curr.next.prev = child

        # Now, we have to connect current to the child list child is currently pointing
        # at the last node of the child list, so we need to use pointer (current.child)
        # to get to the first node of the child list
        curr.next = curr.child
        curr.child.prev = curr

        # At the end remove self.child pointer
        curr.child = None

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solution: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/discuss/1199638/Python-O(n)-O(1)-easy-solution-with-explanation