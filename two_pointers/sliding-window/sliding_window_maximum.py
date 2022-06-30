class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque() # Store indices here
        left, res = 0, []

        # We can use a monotonic queue where it is in decreasing
        # order. We want to maintain this order so we can get
        # the largest number per window. Since the largest
        # value is in the front, we'll only pop when it is
        # out of bounds
        for right, num in enumerate(nums):
            while queue and num > nums[queue[-1]]:
                queue.pop()

            queue.append(right)

            # Remove left-most index from window if out of bounds
            if left > queue[0]:
                queue.popleft()

            # When our window reaches the size of k, we
            # can start appending the results of the
            # max of each subarray
            if right >= k - 1:
                res.append(nums[queue[0]])
                left += 1

        return res

# Time Complexity: O(n) because we iterate through the array once.

# Space Complexity: O(n) because we store the values of our array
# in our queue.

# Solution: https://www.youtube.com/watch?v=DfljaUwZsOk