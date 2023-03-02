class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        dp = [0 for x in range(len(nums))]

        for i in range(2, len(nums)):
            # For every arithmetic we find, we want to increment our result
            if nums[i - 1] - nums[i] == nums[i - 2] - nums[i - 1]:
                # We can use the previous iteration and add it by 1
                dp[i] = dp[i - 1] + 1

        return sum(dp)

# Time Complexity: O(n)
# Time Complexity: O(n)