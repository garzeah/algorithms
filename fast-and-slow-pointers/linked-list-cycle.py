class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        # Determining whether it has a cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

# Time Complexity: Therefore, the time complexity of our algorithm
# will be O(N) where ‘N’ is the total number of nodes in the LinkedList.

# Space Complexity: O(1)

