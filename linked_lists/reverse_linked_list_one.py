class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next # Creating a pointer to next node
            curr.next = prev # Pointing to the previous node
            prev, curr = curr, nxt # Slide the pointers up

        return prev # Prev will be at the start of the reversed list

# Time Complexity: O(n)
# Space Complexity: O(1)