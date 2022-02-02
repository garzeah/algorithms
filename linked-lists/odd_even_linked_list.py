class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        odd = head
        even = head.next
        even_copy = even # Keeping a copy to append to the end of odd

        while odd and even and odd.next and even.next:
            odd.next = even.next # Any value after even is odd
            odd = odd.next # Moving up to the next node

            even.next = odd.next # Any value after odd is even
            even = even.next # Moving up to the next node

        # Appending the end of odd to the start of even
        odd.next = even_copy

        return head

# Time Complexity: O(n)
# Space Complexity: O(1)