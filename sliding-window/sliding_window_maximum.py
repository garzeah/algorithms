    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        output = []

        for i, num in enumerate(nums):
            # We want the largest number in the front
            # so we will pop to maintain this order
            while deque and num >= nums[deque[-1]]:
                deque.pop()

            # Adding the indexes to our deque
            deque.append(i)

            # If our deque is equal to the value outside the window
            if deque[0] == i - k:
                deque.popleft()

            # Once we hit the size of the window we want to
            # append the results to our output array
            if i >= k - 1:
                output.append(nums[deque[0]])

        return output

# Time Complexity: O(n) because for every iteration we check the deque
# a few times but not completely to where it can be considered
# O(n^2)

# Space Complexity: O(n) bc we have 2 arrays that we iterate through
# and keep track of