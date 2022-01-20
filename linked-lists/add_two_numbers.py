class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = curr = ListNode(0)
        carry = 0 # Sum of the values of l1, l2 and carried value

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            curr.next = ListNode(carry % 10) # Appending the result
            curr = curr.next # Move to the next node
            carry //= 10 # Carrying it over to the next value

        return dummy.next

# Time Complexity: O(n)
# Space Complexity: O(n)