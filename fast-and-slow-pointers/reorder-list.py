class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return head

        # Find the middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = self.reverse(slow) # Reversing the second half
        first_half = head

        # Rearrange to produce the LinkedList in the required order
        while first_half is not None and second_half is not None:
            temp = first_half.next
            first_half.next = second_half
            first_half = temp

            temp = second_half.next
            second_half.next = first_half
            second_half = temp

        # Set the next of the last node to 'None'
        if first_half is not None:
            first_half.next = None

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