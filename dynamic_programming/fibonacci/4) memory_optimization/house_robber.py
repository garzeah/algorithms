class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        steal_current = nums[0]
        skip_current = max(nums[0], nums[1])

        for i in range(2, n):
            temp = max(steal_current + nums[i], skip_current)
            steal_current = skip_current
            skip_current = temp

        return skip_current

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solution: https://www.youtube.com/watch?v=73r3KWiEvyk