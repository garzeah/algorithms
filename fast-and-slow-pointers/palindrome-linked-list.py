class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Checking for size 0 or 1
        if head is None or head.next is None:
            return True

        # Find the middle of the linked list
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reversing the second half
        head_second = self.reverse(slow)
        # Store the head of reversed part to revert back later
        copy_head_second = head_second

        # Comparing the both halves and checking if palindrome
        while head and head_second:
            if head.val != head_second.val:
                break

            head = head.next
            head_second = head_second.next

        # Repair the Linked List back to normal
        self.reverse(copy_head_second)

        # Means both halves match (made it
        # through the whole loop without breaking)
        if head is None or head_second is None:
            return True

        return False


    # Reversing the second half
    def reverse(self, head):
        prev = None

        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next

        return prev

# Time Complexity: O(n)
# Space Complexity: O(1)