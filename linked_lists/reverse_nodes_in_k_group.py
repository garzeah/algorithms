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

        prev, curr = None, head
        while k_length != 0:
            # Want to get the last node of the previous sublist and the last
            # node of the current sublist so that we can reverse nodes in
            # groups of k. We can get these values by assigning it to the
            # current prev and curr and reversing it.
            last_prev, last_curr = prev, curr

            # Reversing a k-group
            i = 0
            while curr and i < k:
                nxt = curr.next
                curr.next = prev
                prev, curr = curr, nxt
                i += 1

            # After reversing a group, we are left with a disjointed linked list
            # that is not connected anymore. We have to consider two things:

            # If we have the last node of the previous sublist then that means we have
            # a previous kth group that we have to connect with the current kth group
            if last_prev:
                last_prev.next = prev
            # If we don't have the last node of the previous sublist then that means
            # we just reversed the first kth group and we need to update the head to
            # reflect the new start of the linked list.
            else:
                head = prev

            # Connect the disjointed linked lists
            last_curr.next = curr

            # Update prev so that it's right behind curr for when
            # we reverse the next kth group
            prev = last_curr
            k_length -= 1

        return head

# Time Complexity: O(n)
# Space Complexity: O(1)