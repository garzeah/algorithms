class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [0 for _ in range(len(nums))]
        return self.helper(nums, cache, 0)

    def helper(self, cache, nums, i):
        if i >= len(nums):
            return 0

        if cache[i] == 0:
            # In example [1, 2, 3, 1], we have 2 decisions when trying
            # to find the maximum amount of money we can rob tonight
            # 1) The decision to rob the current house and the remaining
            # houses that are not adjacent to it
            # 2) The decision to rob the adjacent house and the remaining
            # houses that are not adjacent to it
            rob_curr = nums[i] + self.helper(nums, cache, i + 2)
            rob_adj = self.helper(nums, cache, i + 1)

            cache[i] = max(rob_curr, rob_adj)

        return cache[i]

# Time Complexity: O(2^n)
# Space Compelxity: O(n) which is used to store the memoized calls
# Solution: https://www.youtube.com/watch?v=73r3KWiEvyk