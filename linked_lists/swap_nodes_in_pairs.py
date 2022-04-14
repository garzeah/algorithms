class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr and curr.next:
            curr.val, curr.next.val = curr.next.val, curr.val
            curr = curr.next.next; # Heads to the next node that needs to be swapped

        return head

# Time Complexity: O(n)
# Space Complexity: O(1)