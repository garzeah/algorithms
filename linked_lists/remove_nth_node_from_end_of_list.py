# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # We can use two pointers to remove the nth node by starting
        # left and right at the same spot and moving right n times.
        # We then can move left and right until left is before the
        # node we want to remove.
        left, right = head, head

        # Moving right n times
        for _ in range(n):
            right = right.next

        # After n iterations, if right isn't at a node then that means
        # we are removing the 1st node. It's an edge case for linked
        # lists like [1], n = 1
        if right is None:
            return head.next

        # Want to move left right before the node we want to remove
        while right.next:
            left = left.next
            right = right.next

        left.next = left.next.next # Removing node

        return head

# Time Complexity: O(n)
# Space Complexity: O(1)