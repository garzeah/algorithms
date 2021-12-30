class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Used to keep track of the highest index
        # ordered from greatest to least
        deque = collections.deque()
        res = []

        for end, num in enumerate(nums):
            # Making sure it is ordered from greatest to least
            # If the last number is <= num then we want to pop
            # and put that current number in the front
            while deque and num >= nums[deque[-1]]:
                deque.pop()

            # Adding the indexes into our deque
            deque.append(end)

            # Remove first element if it's outside the window
            # AKA sliding the window
            if deque[0] == end - k:
                deque.popleft()

            # When our window reaches the size of k,
            # then we want to add to results
            if end >= k - 1:
                res.append(nums[deque[0]])

        return res

# Time Complexity: O(n) because for every iteration we check the deque
# a few times but not completely to where it can be considered
# O(n^2)

# Space Complexity: O(n) bc we have 2 arrays that we iterate through
# and keep track of