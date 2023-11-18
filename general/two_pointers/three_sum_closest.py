class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = float('inf')

        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1

            while (left < right):
                target_diff = target - nums[i] - nums[left] - nums[right]

                # We've found a triplet with an exact sum
                if target_diff == 0:
                    return target

                # The second part of the following 'if' is to handle the
                # smallest sum when we have more than one solution
                if abs(target_diff) < abs(min_diff):
                    # Save the new closest target difference
                    min_diff = target_diff

                if target_diff > 0:
                    # We need to subtract a bigger triplet to get to 0
                    left += 1
                else:
                    # We need to subtract a smaller triplet to get to 0
                    right -= 1

        # Return the closest sum of 3 numbers to target
        return target - min_diff

# Time Complexity: Sorting the array will take O(N* logN).
# Overall, the function will take O(N * logN + N^2)
# which is asymptotically equivalent to O(N^2)

# Space Complexity: The above algorithm’s space complexity
# will be O(N), which is required for sorting.