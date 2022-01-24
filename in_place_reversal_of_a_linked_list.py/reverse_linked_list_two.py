# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        # After skipping 'p-1' nodes, current will point to 'p'th node
        curr, prev = head, None
        i = 0
        while curr is not None and i < left - 1: # Want to be at p - 1
            prev = curr
            curr = curr.next
            i += 1

        # We are interested in three parts of the LinkedList, the part before index 'p',
        # the part between 'p' and 'q', and the part after index 'q'
        last_node_of_first_part = prev

        # After reversing the LinkedList 'curr' will become the last node of the sub-list
        last_node_of_sub_list = curr

        # Will be used to temporarily store the next node
        next = None

        i = 0
        # Reverse nodes between 'p' and 'q'
        while curr and i < right - left + 1:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            i += 1

        # Connect with the first part
        if last_node_of_first_part:
            # 'prev' is now the first node of the sub-list
            last_node_of_first_part.next = prev
        # This means p == 1 i.e., we are changing the first node (head) of the LinkedList
        else:
            head = prev

        # Connect with the last part
        last_node_of_sub_list.next = curr
        return head

# Time Complexity: O(n)
# Space Complexity: O(1)