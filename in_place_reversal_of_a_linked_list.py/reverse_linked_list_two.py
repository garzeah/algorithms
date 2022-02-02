# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        # After skipping 'left - 1' nodes, current will point to 'left'th node
        prev, curr = None, head
        i = 0
        while curr and i < left - 1: # Want to be at left - 1
            prev = curr
            curr = curr.next
            i += 1

        # We are interested in three parts of the LinkedList, the part before index 'left',
        # the part between 'left' and 'right', and the part after index 'right'
        last_node_of_pre_sub_list = prev

        # After reversing the LinkedList 'curr' will become the last node of the sub-list
        last_node_of_sub_list = curr

        i = 0
        # Reverse nodes between 'left' and 'right'
        while curr and i < right - left + 1:
            temp_next = curr.next # Temporarily store the next node
            curr.next = prev # Reverse the current node
            prev = curr # Before we move to the next node, point previous to the current node
            curr = temp_next # Move on the next node
            i += 1

        # Connect pre-sub-list with start of sub-list
        if last_node_of_pre_sub_list:
            last_node_of_pre_sub_list.next = prev
        # Usually do this when the start and prev node overlap
        else:
            head = prev

        # Since we reversed, curr will point to the first node post sub-list
        last_node_of_sub_list.next = curr

        return head

# Time Complexity: O(n)
# Space Complexity: O(1)