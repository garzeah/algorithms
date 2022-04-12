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
                # Need to add i because arrays are compared position by position:
                # The first item of the first array is compared to the first item
                # of the second array; if they are not equal (i.e. the first is
                # greater or smaller than the second) then that's the result of
                # the comparison, else if they are equal the second item is
                # considered, then the third and so on.
                heappush(min_heap, [head.val, i, head])

        while min_heap:
            val, i, node = min_heap[0]

            if node.next is None: # We've exhausted a linked list
                heappop(min_heap)
            else:
                # heapreplace(a, x) returns the smallest value
                # originally in a regardless of the value of x
                heapreplace(min_heap, [node.next.val, i, node.next])

            curr.next = node
            curr = curr.next

        return dummy.next

# Time Complexity: Since we’ll be going through all the elements of all arrays and
# will be removing/adding one element to the heap in each step, the time complexity
# of the above algorithm will be O(N*logK), where ‘N’ is the total number of
# elements in all the ‘K’ input arrays.

# Space Complexity: The space complexity will be O(K) because, at any time, our
# min-heap will be storing one number from all the ‘K’ input arrays.

# Solution: https://www.youtube.com/watch?v=kpCesr9VXDA