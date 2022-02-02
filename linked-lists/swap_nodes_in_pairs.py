class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr and curr.next:
            self.swap(curr, curr.next)
            curr = curr.next.next; # Heads to the next node that needs to be swapped

        return head

    def swap(self, node1, node2):
        temp = node1.val
        node1.val = node2.val
        node2.val = temp

# Time Complexity: O(n)
# Space Complexity: O(1)