class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        return max(
            self.rob_recursive(nums[1:]),
            self.rob_recursive(nums[:-1])
        )

    # Since it's circular and the first and last houses
    # are considered adjacent, we can just take the max
    # of everything but the first and everything but
    # the last and return that
    def rob_recursive(self, nums):
        steal_current = nums[0]
        skip_current = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            temp = max(steal_current + nums[i], skip_current)
            steal_current = skip_current
            skip_current = temp

        return skip_current

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solution: https://www.youtube.com/watch?v=rWAJCfYYOvM