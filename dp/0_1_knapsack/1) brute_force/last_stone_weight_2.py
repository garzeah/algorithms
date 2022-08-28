class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        return self.helper(stones, 0, 0, 0)

    def helper(self, stones, x, y, i):
        if i == len(stones):
            return abs(y - x)

        diff_1 = self.helper(stones, x + stones[i], y, i + 1)
        diff_2 = self.helper(stones, x, y + stones[i], i + 1)

        return min(diff_1, diff_2)

# Solution: https://leetcode.com/problems/last-stone-weight-ii/discuss/1445462/Python-or-DP-or-Memoizationor-Minimumm-Subset-Sum-Difference