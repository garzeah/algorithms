# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        # If we had 2 rotations, then we want to find the
        # last 2 nodes and put it at the beginning and
        # connect it to the start of the linked list.
        # We also have to remove the connections
        # they had prior to the new connection.

        # Want to get the last node so we can connect it
        # to the start of the linked list
        last = head
        length = 1
        while last.next:
            last = last.next
            length += 1

        k = k % length # Modulus in the event k > len(linked_list)
        last.next = head # Connecting to the start

        # Want to break the cycle by stopping just before the
        # node(s) we just swapped. Also, we substract by 1 bc
        # we start counting at 1 instead of 0
        curr = head
        for _ in range(length - k - 1):
            curr = curr.next

        start = curr.next
        curr.next = None # Removing old connection

        return start

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solution: https://www.youtube.com/watch?v=UcGtPs2LE_c