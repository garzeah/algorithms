class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        triplets = []

        for i in range(len(nums)):
            # Skip same element to avoid duplicate quadruplets
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            for j in range(i + 1, len(nums)):
                # Skip same element to avoid duplicate quadruplets
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue

                left, right = j + 1, len(nums) - 1

                while left < right:
                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if curr_sum == target:
                        triplets.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left - 1] == nums[left]:
                            left += 1
                        while left < right and nums[right + 1] == nums[right]:
                            right -= 1
                    elif curr_sum < target:
                        left += 1
                    else:
                        right -= 1

        return triplets

# Time Complexity: Sorting the array will take O(N*logN). Overall
# searchQuadruplets() will take O(N * logN + N^3), which is
# asymptotically equivalent to O(N^3).

# Space Complexity: The space complexity of the above algorithm
# will be O(N) which is required for sorting.