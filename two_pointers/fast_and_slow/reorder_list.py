class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reversing the second half from the middle
        left, right = head, self.reverse(slow)

        # Rearrange to produce the LinkedList in the required order
        while left and right:
            nxt = left.next
            left.next = right # Assign new value
            left = nxt # Slide pointer up

            nxt = right.next
            right.next = left # Assign new value
            right = nxt # Slide pointer up

        # In the event our linked list is even in length, left
        # will still be pointing to a node so we need to clear it
        if left:
            left.next = None

        return head

    def reverse(self, curr):
        prev = None

        while curr:
            nxt = curr.next # Temporarily store the next node
            curr.next = prev # Reverse the current node
            prev = curr # Before we move to the next node, point previous to the current node
            curr = nxt # Move on the next node

        return prev

# Time Complexity: O(n)
# Space Complexity: (1)
# Solution: https://www.youtube.com/watch?v=S5bfdUTrKLM