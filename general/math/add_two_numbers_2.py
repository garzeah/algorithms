# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = self.reverse(l1), self.reverse(l2)
        dummy = curr = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next

            if l2:
                carry += l2.val
                l2 = l2.next

            curr.next = ListNode(carry % 10)
            curr = curr.next
            carry //= 10

        return self.reverse(dummy.next)

    def reverse(self, head):
        prev = None

        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev

# Time Complexity: O(n)
# Space Complexity: O(1)