# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 1 or head is None:
            return head

        curr = head
        k_length = 0

        # Calculating the number of k-groups in our linked list
        while curr:
            curr = curr.next
            k_length += 1

        k_length //= k

        curr, prev = head, None
        while k_length != 0:
            last_node_of_prev_part = prev

            # After reversing the LinkedList 'curr' will become the last node of the sub-list
            last_node_of_sub_list = curr
            i = 0

            while curr and i < k:  # Reverse 'k' nodes
                temp_next = curr.next # Temporarily store the next node
                curr.next = prev # Reverse the current node
                prev = curr # Before we move to the next node, point previous to the current node
                curr = temp_next # Move on the next node
                i += 1

            # Connect with the previous part
            if last_node_of_prev_part:
                last_node_of_prev_part.next = prev
            else:
                head = prev

            # Connect with the next part
            last_node_of_sub_list.next = curr

            # Assign the last node of the previous sub list to prev
            prev = last_node_of_sub_list
            k_length -= 1
        return head

# Time Complexity: O(n)
# Space Complexity: O(1)