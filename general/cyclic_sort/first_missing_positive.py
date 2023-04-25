class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
      i, n = 0, len(nums)
      while i < n:
        j = nums[i] - 1

        # Only want to sort if it's within the range of [0, n].
        # If it isn't, then we can assume the first missing
        # positive is the first number (1)
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
          nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
          i += 1

      for i in range(n):
        if nums[i] != i + 1:
          return i + 1

        # Edge case for numbers like [1], the first missing
        # positive would be 2 so we can just return the n + 1
      return n + 1

# Time Complexity: O(n)
# Space Complexity: O(1)