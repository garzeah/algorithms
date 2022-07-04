class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Referencing the same address in memory
        dummy = curr = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1 # Assign the next node to the current l1 node
                l1 = l1.next # Point to the next node
            else:
                curr.next = l2 # Assign the next node to the current l2 node
                l2 = l2.next # Point to the next node

            # Head to the last node
            curr = curr.next

        # Assign the remaining node since one of them will end first
        curr.next = l1 or l2

        # Returning the node after ListNode(0)
        return dummy.next

# Time Complexity: O(n)
# Space Complexity: O(n)