class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        curr_path, output = [], []
        self.backtrack(nums, 0, curr_path, output)
        return output

    def backtrack(self, nums, i, curr_path, output):
        if i == len(nums):
            output.append(list(curr_path))
            return

        # All subsets that include nums[i]
        curr_path.append(nums[i])
        self.backtrack(nums, i + 1, curr_path, output)
        curr_path.pop()

        # All subsets that don't include nums[i]
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        self.backtrack(nums, i + 1, curr_path, output)

# Time Complexity: Since, in each step, the number of subsets doubles (if not duplicate) as
# we add each element to all the existing subsets, therefore, we will have a total of
# O(2^N) subsets, where ‘N’ is the total number of elements in the input set. And
# since we construct a new subset from an existing set, therefore, the time
# complexity of the above algorithm will be O(N*2^N).

# Space Complexity: All the additional space used by our algorithm is for the output list.
# Since, at most, we will have a total of O(2^N) subsets, and each subset can take up to
# O(N) space, therefore, the space complexity of our algorithm will be O(N*2^N).