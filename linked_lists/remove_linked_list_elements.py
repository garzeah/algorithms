class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            if curr.val == val:
                if prev: # If we want to remove the node past the start
                    prev.next = curr.next
                else: # If we want to remove the first node
                    head = curr.next

                # Move it up, so we don't have a reference
                # to the removed node in the next loop
                curr = curr.next
            else: # Move it up since no match
                prev, curr = curr, curr.next

        return head

    # Time Complexity: O(n)
    # Space Complexity: O(1)