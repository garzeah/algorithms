# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = curr = ListNode(0)
        min_heap = []

        # Put the value of the heads in the min heap so we don't
        # need to push more than 'k' elements in the heap
        for i, head in enumerate(lists):
            if head:
                # Need to add i because the problem with adding ListNode objects as tasks
                # is that the Tuple comparison breaks for (value, task) pairs if the
                # values are equal and the tasks do not have a default comparison
                # order. The solution is to store entries as 3-element list
                # including the value, an index count (i), and the task.
                heappush(min_heap, [head.val, i, head])

        while min_heap:
            val, i, node = min_heap[0]

            curr.next = node
            curr = curr.next

            # We've exhausted a linked list
            if node.next is None:
                continue

            # Check the next value in the node
            heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next

# Time Complexity: O(N * K * log(k)) since the while loop will run for as many nodes
# there are in the linked lists which is O(N * K) where N is the length of the list
# and k is the amount of linked lists. Heappop and heappush take O(log(k)) time
# since we'll have at most k linked lists in our heap.

# Space Complexity: The space complexity will be O(N * K) where N is the amount of
# nodes in a list and K is the total amount of linked lists.

# Solution: https://leetcode.com/problems/merge-k-sorted-lists/discuss/10513/108ms-python-solution-with-heapq-and-avoid-changing-heap-size