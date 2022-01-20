class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left, right = head, head

        # Now left and right will be at difference n
        for _ in range(n):
            right = right.next

        # Only happens when removing the first element
        if right == None:
            return head.next

        # Will take us right before the node we want to remove
        while right.next != None:
            left = left.next
            right = right.next

        # Removing the node
        left.next = left.next.next

        return head

# Time Complexity: O(n)
# Space Complexity: O(1)