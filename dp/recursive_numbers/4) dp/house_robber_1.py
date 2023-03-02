class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        rob_curr = nums[0]
        rob_adj = max(nums[0], nums[1])

        for i in range(2, n):
            temp = max(rob_curr + nums[i], rob_adj)
            rob_curr = rob_adj
            rob_adj = temp

        return rob_adj

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solution: https://www.youtube.com/watch?v=73r3KWiEvyk