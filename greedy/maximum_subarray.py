class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, curr_sum = nums[0], 0

        # We can take a greedy approach by choosing the most
        # optimal local sum as we iterate thru the array. We
        # can make this more optimal by resetting the sum to
        # 0 whenever we encounter a negative number since it
        # won't help with getting the best local sum
        for num in nums:
            # Resetting the curr_sum to 0 if negative
            if curr_sum < 0:
                curr_sum = 0

            curr_sum += num
            max_sum = max(max_sum, curr_sum)

        return max_sum

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solution: https://www.youtube.com/watch?v=5WZl3MMT0Eg