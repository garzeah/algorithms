# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # After skipping 'left - 1' nodes, current will point to 'left'th node
        curr, prev = head, None
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
        # curr will end at the first value at the end of the sublist
        # prev will be at the start of the reversed portion
        while curr and i < right - left + 1:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            i += 1

        # Connect pre-sub-list with sub-list
        if last_node_of_pre_sub_list:
            # Since we reversed, prev will point to the first node in the sub-list
            last_node_of_pre_sub_list.next = prev
        else: # The sublist starts at left = 1 so replace the head with prev
            head = prev

        # Since we reversed, curr will point to the first node post sub-list
        last_node_of_sub_list.next = curr
        return head

# Time Complexity: O(n)
# Space Complexity: O(1)