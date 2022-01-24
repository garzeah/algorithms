class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i, n = 0, len(nums)
        output = []

        while i < n:
            # Range is 1 to n, so we have dont have
            # to ignore n since we can place it in the array
            j = nums[i] - 1

            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i in range(n):
            # Checking if it each value is in the correct spot
            if nums[i] != i + 1:
                # Appending the missing number
                output.append(i + 1)

        return output

    # Time Complexity: O(n)
    # Space Complexity: O(1)