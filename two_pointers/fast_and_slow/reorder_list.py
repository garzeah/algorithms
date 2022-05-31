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
            temp_next = left.next
            left.next = right # Assign new value
            left = temp_next # Slide pointer up

            temp_next = right.next
            right.next = left # Assign new value
            right = temp_next # Slide pointer up

        # In the event our linked list is even in length, left
        # will still be pointing to a node so we need to clear it
        if left:
            left.next = None

        return head

    def reverse(self, head):
        prev = None

        while head:
            next = head.next # Temporarily store the next node
            head.next = prev # Reverse the current node
            prev = head # Before we move to the next node, point previous to the current node
            head = next # Move on the next node

        return prev

# Time Complexity: O(n)
# Space Complexity: (1)
# Solution: https://www.youtube.com/watch?v=S5bfdUTrKLM