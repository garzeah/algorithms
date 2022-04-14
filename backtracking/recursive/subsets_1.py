class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr_path, output = [], []
        return self.backtrack(nums, 0, curr_path, output)

    def backtrack(self, nums, i, curr_path, output):
        # Base Case, means we are out of bounds
        if i == len(nums):
            output.append(list(curr_path))
            return

        # Decision to include nums[i]
        curr_path.append(nums[i])
        self.backtrack(nums, i + 1, curr_path, output)

        # Decision to not include nums[i]
        curr_path.pop()
        self.backtrack(nums, i + 1, curr_path, output)

        return output

# Time Complexity: O(n*2^n), where n is the amount of numbers we have
# in our array and 2^n is because of the decision tree, for each
# we have, it doubles as we hit the next level of our tree.

# Space Complexity: All the additional space used by our algorithm is
# for the output list. Since we will have a total of O(2^N) subsets,
# and each subset can take up to O(N) space, therefore, the space
# complexity of our algorithm will be O(N*2^N).

# Solution: https://www.youtube.com/watch?v=REOH22Xwdkk