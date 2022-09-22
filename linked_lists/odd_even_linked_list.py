class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        # Keeping a copy to append to beginning off even to the end of odd
        odd = head
        even = even_copy = head.next

        # Since even is ahead, we just have to make sure we
        # have both a valid even and even.next node. Since
        # 1st and 2nd node is respectively odd and even,
        # we can take advantage of this relationship to
        # build a linked list
        while even and even.next:
            odd.next = even.next # Any value after even is odd
            odd = odd.next # Moving up to the next node so next is even

            even.next = odd.next # Any value after odd is even
            even = even.next # Moving up to the next node so next is odd

        # Appending the end of odd to the start of even
        odd.next = even_copy

        return head

# Time Complexity: O(n)
# Space Complexity: O(1)