class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        curr_path, output = [], []
        self.backtrack(candidates, target, 0, curr_path, 0, output)
        return output

    def backtrack(self, candidates, target, i, curr_path, total_sum, output):
        # In the event our index or total sum gets to large, return
        if i >= len(candidates) or total_sum > target:
            return

        # We found a sum, record it!
        if total_sum == target:
            output.append(list(curr_path))
            return

        # Finding combinations on the left side of the tree
        curr_path.append(candidates[i])
        self.backtrack(candidates, target, i, curr_path, total_sum + candidates[i], output)

        # When we pop the value, shift i by one so it doesn't include
        # the prior value in order to prevent duplicates
        curr_path.pop()
        self.backtrack(candidates, target, i + 1, curr_path, total_sum, output)

# Time Complexity: O(2^t) where t is the target value since at most our
# decision tree can reach a height of t with the levels either growing
# or getting smaller.

# Space Complexity: ?

# Solution: https://www.youtube.com/watch?v=GBKI9VSKdGg
