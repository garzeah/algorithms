class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output, subset = [], []
        return self.dfs(0, nums, subset, output)

    def dfs(self, i, nums, subset, output):
        # Base Case, means we are out of bounds
        if i >= len(nums):
            output.append(subset.copy())
            return

        # Decision to include nums[i]
        subset.append(nums[i])
        self.dfs(i + 1, nums, subset, output)

        # Decision to not include nums[i]
        subset.pop()
        self.dfs(i + 1, nums, subset, output)

        return output

# Time Complexity: O(n*2^n), where n is the amount of numbers we have
# in our array and 2^n is because of the decision tree, for each
# we have, it doubles as we hit the next level of our tree.

# Space Complexity: All the additional space used by our algorithm is
# for the output list. Since we will have a total of O(2^N) subsets,
# and each subset can take up to O(N) space, therefore, the space
# complexity of our algorithm will be O(N*2^N).