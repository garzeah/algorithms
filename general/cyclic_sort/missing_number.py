class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i, n = 0, len(nums)

        while i < n:
            # Range is 0 to n - 1, so we have to ignore
            # n since we can't place it in the array
            j = nums[i]


            # Do not want to map to n which is
            # why we have nums[i] < n
            if nums[i] < n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1


        for i in range(n):
            # If no match, that is our missing number
            if nums[i] != i:
                return i

        return n

# Time Complexity: O(n)
# Space Complexity: O(1)