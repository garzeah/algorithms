class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left, right = head, head

        # Now left and right will be at difference n
        for _ in range(n):
            right = right.next

        # If we don't have space to iterate through early
        # because we pass in a small linked list then we
        # want to remove the beginning of the linked list
        if right is None:
            return head.next

        # Will take us right before the node we want to remove
        while right.next:
            left = left.next
            right = right.next

        # Removing the node
        left.next = left.next.next

        return head

# Time Complexity: O(n)
# Space Complexity: O(1)