class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Sort the numbers to handle duplicates
        nums.sort()
        subsets = [[]]
        start, end = 0, 0
        for i in range(len(nums)):
            start = 0 # Resets in the event of no duplicate

            # If current and the previous elements are same, create new
            # subsets only from the subsets added in the previous step
            if i > 0 and nums[i - 1] == nums[i]:
                # We are using the previous end to get the start
                # of the subsets added in the previous step
                start = end + 1

            end = len(subsets) - 1

            for j in range(start, end + 1):
                # Create a new subset from the existing subset
                # and add the current element to it
                temp_set = list(subsets[j])
                temp_set.append(nums[i])
                subsets.append(temp_set)

        return subsets

# Time Complexity: O(n * 2^n)
# Space Complexity: O(n * 2^n)