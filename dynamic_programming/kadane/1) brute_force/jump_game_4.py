class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # So for every number we encounter, we can add it with
        # the maximum of k previous numbers and store it so
        # we can re-use for future iterations
        # [1, -1, -2, 4, -7, 3], k = 2
        # [1, 0, -1, 4, -3, 7]

        # [10,-5,-2,4,0,3], k = 3
        # [10, 5, 8, 14, 14, 17]

        dp = [0 for x in range(len(nums))]
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            max_val = float('-inf')

            # We want to find the max value that is before k jumps
            for j in range(i - k, i):
                if j >= 0:
                    max_val = max(max_val, dp[j])

            # Adding the score of the current index with maximum score
            dp[i] = max_val + nums[i]

        return dp[-1]


# Time Complexity: O(n * logn)
# Space Complexity: O(n)
# Solution: https://leetcode.com/problems/jump-game-vi/discuss/2258517/python-solution-(DP-%2B-heap)-with-explanation