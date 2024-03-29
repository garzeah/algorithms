class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        # Slow will always stop at the middle whenever
        # fast finishes
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

# Time Complexity: O(n)
# Space Complexity: O(1)