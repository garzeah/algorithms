class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            temp_next = head.next # Temporarily store the next node
            head.next = prev # Reverse the current node
            prev = head # Before we move to the next node, point previous to the current node
            head = temp_next # Move on the next node

        return prev

# Time Complexity: O(n)
# Space Complexity: O(1)