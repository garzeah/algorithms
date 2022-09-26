class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next # Make a copy of the next node
            curr.next = prev # Reverse node by pointing curr.next to prev
            prev, curr = curr, nxt # Move up prev and curr so we can reverse the next node

        return prev # Prev will be at the start of the reversed list

# Time Complexity: O(n)
# Space Complexity: O(1)