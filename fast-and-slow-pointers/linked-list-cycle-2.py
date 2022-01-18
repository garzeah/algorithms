class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        cycle_length = 0

        # Determining whether it has a cycle or not
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                cycle_length = Solution.calculate_cycle_length(slow)
                break

        return Solution.find_start(head, cycle_length)

    def calculate_cycle_length(slow):
        curr = slow
        cycle_length = 0

        while True:
            curr = curr.next
            cycle_length += 1

            # Once it equals the beginning, break because
            # we are at the start of the cycle
            if curr == slow:
                break

        return cycle_length

    def find_start(head, cycle_length):
        pointer1 = head
        pointer2 = head

        # Move pointer2 ahead 'cycle_length' nodes
        while cycle_length > 0:
            pointer2 = pointer2.next
            cycle_length -= 1

        # Increment both pointers until they meet at the
        # start of the cycle
        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        return pointer1

# Time Complexity: O(n)
# Space Complexity: O(1)