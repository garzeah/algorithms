class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            if prev and prev.val == curr.val:
                if prev:
                    prev.next = curr.next
                curr = curr.next # Move up pointer in the event of other pointers
            else: # Nothing needs to be removed, keep iterating
                prev, curr = curr, curr.next

        return head

    # Time Complexity: O(n)
    # Space Complexity: O(1)