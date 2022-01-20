class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            if curr.val == val:
                # If Node to remove is at the end or in the middle
                if prev: # Will "delete" the node
                    prev.next = curr.next
                else: # If Node to remove is at the start
                    # Will "delete" the node by setting it to the next value
                    head = curr.next
                curr = curr.next
            else:  # Nothing needs to be removed, keep iterating
                prev, curr = curr, curr.next

        return head

    # Time Complexity: O(n)
    # Space Complexity: O(1)