class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque() # Indices
        output = []
        l = r = 0

        while r < len(nums):
            # While smaller values exist in our queue,
            # we want to pop them out since we have
            # access to a higher value already
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()

            queue.append(r)

            # Remove left-most index from window if out of bounds
            if l > queue[0]:
                queue.popleft()

            # When our window reaches the size of k, we
            # can start appending the results of the
            # max of each subarray
            if (r + 1) >= k:
                output.append(nums[queue[0]])
                l += 1

            r += 1

        return output

# Time Complexity: O(n) because we iterate through the array once.

# Space Complexity: O(n) because we store the values of our array
# in our queue.

# Solution: https://www.youtube.com/watch?v=DfljaUwZsOk