class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # Our key will be x#y
        dp = [{} for x in range(len(stones) + 1)]
        return self.helper(stones, dp, 0, 0, 0)

    def helper(self, stones, dp, x, y, i):
        if i == len(stones):
            return abs(y - x)

        # Building our key
        key = str(x) + '#' + str(y)

        if key not in dp[i]:
            diff_1 = self.helper(stones, dp, x + stones[i], y, i + 1)
            diff_2 = self.helper(stones, dp, x, y + stones[i], i + 1)
            dp[i][key] = min(diff_1, diff_2)

        return dp[i][key]

# Time Complexity: O(n * m) where n is the amount of stones
# and m is the amount of sums we calculate

# Space Complexity: O(n * m) where n is the amount of stones
# and m is the amount of sums we calculate

# Solution: https://leetcode.com/problems/last-stone-weight-ii/discuss/1445462/Python-or-DP-or-Memoizationor-Minimumm-Subset-Sum-Difference

