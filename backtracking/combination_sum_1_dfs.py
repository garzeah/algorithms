class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        curr_nums, output = [], []
        self.dfs(candidates, target, 0, curr_nums, 0, output)
        return output

    def dfs(self, candidates, target, i, curr_nums, total_sum, output):
        # Base Case
        if total_sum == target:
            output.append(list(curr_nums))
            return

        if i >= len(candidates) or total_sum > target:
            return

        curr_nums.append(candidates[i])
        self.dfs(candidates, target, i, curr_nums, total_sum + candidates[i], output)

        curr_nums.pop()
        self.dfs(candidates, target, i + 1, curr_nums, total_sum, output)

# Time Complexity: O(2^t) where t is the target value since at most our
# decision tree can reach a height of t with the levels either growing
# or getting smaller.

# Space Complexity: ?

# Solution: https://www.youtube.com/watch?v=GBKI9VSKdGg
