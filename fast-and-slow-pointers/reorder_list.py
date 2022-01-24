class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return head

        # Find the middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reversing the second half from the middle
        left, right = head, self.reverse(slow)


        # Rearrange to produce the LinkedList in the required order
        while left is not None and right is not None:
            next = left.next
            left.next = right
            left = next

            next = right.next
            right.next = left
            right = next

        # Set the next of the last node to 'None'
        # in 1,2,3,4 --> 1,4,2,3 we want 3 to point to nothing
        # otherwise we get a cycle
        if left is not None:
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