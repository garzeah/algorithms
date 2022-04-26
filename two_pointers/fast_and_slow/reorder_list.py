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
            # left will point to the last node
            temp_next = left.next
            left.next = right
            left = temp_next

            temp_next = right.next
            right.next = left
            right = temp_next

        # If linked list length is odd -> it's already none
        # If linked list length is even -> we need to set
        # last node to none or we have a cycle
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
# Space Complexity(1)