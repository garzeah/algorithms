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

        # Edge case: What to do when values goes beyond the length of the
        # linked list. If this happens then we want the closest value
        # counting from the end of the list. We can resolve this by
        # returning head.next since we'll always want to remove the
        # head in this scenario
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