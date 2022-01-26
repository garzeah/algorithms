# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = head
        k_length = 0

        # Calculating the number of k-groups in our linked list
        while dummy:
            dummy = dummy.next
            k_length += 1

        k_length //= k

        curr, prev = head, None
        while k_length != 0:
            last_node_of_prev_part = prev

            # After reversing the LinkedList 'curr' will become the last node of the sub-list
            last_node_of_sub_list = curr
            i = 0

            while curr and i < k:  # Reverse 'k' nodes
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                i += 1

            # Connect with the previous part
            if last_node_of_prev_part:
                last_node_of_prev_part.next = prev
            else:
                head = prev

            # Connect with the next part
            last_node_of_sub_list.next = curr

            if curr is None:
                break
            prev = last_node_of_sub_list
            k_length -= 1
        return head

# Time Complexity: O(n)
# Space Complexity: O(1)