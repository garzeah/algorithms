# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        h1 = l1 = ListNode(0)
        h2 = l2 = ListNode(0)

        # Want to get every value to the left of x
        # and every value to the right of x then
        # connect left with right
        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next

        l2.next = None # Avoiding cycles
        l1.next = h2.next # Connecting left and right
        return h1.next

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solution: https://www.youtube.com/watch?v=KT1iUciJr4g