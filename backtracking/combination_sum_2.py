class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        return self.backtrack(sorted(candidates), target, 0, [], output)

    def backtrack(self, candidates, target, start, curr_path, output):
        # Found a match
        if target == 0:
            output.append(list(curr_path))
            return

        # Invalid match
        if target < 0:
            return

        # Performing dfs and handling duplicates
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue

            curr_path.append(candidates[i])
            self.backtrack(candidates, target - candidates[i], i + 1, curr_path, output)
            curr_path.pop()

        return output

# Time Complexity: O(N*2^t) where t is the target value since at most our
# decision tree can reach a height of t with the levels either growing
# or getting smaller.

# Space Complexity: ?

# Solution: https://www.youtube.com/watch?v=rSA3t6BDDwg