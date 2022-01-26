class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reversing the second half from the middle
        left, right = head, self.reverse(slow)

        # Rearrange to produce the LinkedList in the required order
        while left and right:
            # left will point to the last node
            next = left.next
            left.next = right
            left = next

            next = right.next
            right.next = left
            right = next

        # If linked list length is even -> we need to set
        # last node to none or we have a cycle

        # If linked list length is odd -> it's already none
        if left:
            left.next = None

    def reverse(self, head):
        prev = None

        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next

        return prev

# Time Complexity: O(n)
# Space Complexity(1)