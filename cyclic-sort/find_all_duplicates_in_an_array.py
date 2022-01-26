class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i, n = 0, len(nums)
        output = []

        while i < n:
            j = nums[i] - 1

            if nums[i] <= n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                output.append(nums[i])

        return output

# Time Complexity: O(n)
# Space Complexity: O(1)