class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        left = head
        # Reversing the second half
        right = self.reverse(slow)
        # Store the head of reversed part to revert back later
        right_copy = right

        # Comparing the both halves and checking if palindrome
        while left and right:
            if left.val != right.val:
                break

            left = left.next
            right = right.next

        # Repair the Linked List back to normal
        self.reverse(right_copy)

        # Means both halves match (made it
        # through the whole loop without breaking)
        if right is None:
            return True

        return False


    # Reversing the second half
    def reverse(self, head):
        prev = None

        while head:
            next = head.next # Temporarily store the next node
            head.next = prev # Reverse the current node
            prev = head # Before we move to the next node, point previous to the current node
            head = next # Move on the next node

        return prev

# Time Complexity: O(n)
# Space Complexity: O(1)