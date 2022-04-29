class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        curr_path, output = [], []
        return self.backtrack(candidates, target, 0, curr_path, output)

    def backtrack(self, candidates, target, start, curr_path, output):
        # When target is equal to 0, we have found a valid combination
        if target == 0:
            output.append(list(curr_path))
            return

        # Invalid combination
        if target < 0:
            return

        # Performing dfs on each candidate
        for i in range(start, len(candidates)):
            curr_path.append(candidates[i])
            self.backtrack(candidates, target - candidates[i], i, curr_path, output)
            curr_path.pop()

        return output

# Time Complexity: O(N*2^t) where t is the target value since at most our
# decision tree can reach a height of t with the levels either growing
# or getting smaller.

# Space Complexity: ?

# Solution: https://www.youtube.com/watch?v=GBKI9VSKdGg
