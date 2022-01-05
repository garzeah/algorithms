class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []

        for i in range(len(nums)):
            # If we encounter a duplicate then skip
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                # These will be used to find a triplet that equals 0
                curr_sum = nums[left] + nums[right]
                target_sum = -nums[i]

                # If we added current_sum and target_sum
                # together we would get 0
                if curr_sum == target_sum:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Preventing duplicates by checking if the previous
                    # values are the same number
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
                    while left < right and nums[right + 1] == nums[right]:
                        right -= 1
                # Since this is sorted it means we want a bigger current_sum
                elif target_sum > curr_sum:
                    left += 1
                # Since this is sorted it means we want a smaller current_sum
                else:
                    right -= 1

        return triplets

# Time Complexity: O(n^2) b/c for every i, we are searching all of
# the values after it

# Space Complexity: O(n) bc we have to sort the array