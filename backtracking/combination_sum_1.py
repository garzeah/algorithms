class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        curr_path, output = [], []
        return self.backtrack(candidates, target, 0, 0, curr_path, output)

    def backtrack(self, candidates, target, i, total_sum, curr_path, output):
        # In the event our index or total sum gets to large, return
        if i >= len(candidates) or total_sum > target:
            return

        # We found a sum, record it!
        if total_sum == target:
            output.append(list(curr_path))
            return

        # Decision to include candidates[i]
        curr_path.append(candidates[i])
        self.backtrack(candidates, target, i, total_sum + candidates[i], curr_path, output)

        # Decision to not include candidates[i]
        curr_path.pop()
        self.backtrack(candidates, target, i + 1, total_sum, curr_path, output)

        return output

# Time Complexity: O(N*2^t) where t is the target value since at most our
# decision tree can reach a height of t with the levels either growing
# or getting smaller.

# Space Complexity: ?

# Solution: https://www.youtube.com/watch?v=GBKI9VSKdGg
