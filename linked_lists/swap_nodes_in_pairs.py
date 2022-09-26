# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr and curr.next:
            # Save pointers
            start_of_next_pair = curr.next.next
            second = curr.next

            # Reverse this pair
            second.next = curr
            curr.next = start_of_next_pair
            prev.next = second

            # Update Pointers
            prev = curr
            curr = start_of_next_pair

        return dummy.next

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solution: https://www.youtube.com/watch?v=o811TZLAWOo