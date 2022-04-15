class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        curr_path, output = [], []
        self.backtrack(candidates, target, 0, curr_path, output)
        return output

    def backtrack(self, candidates, target, start, curr_path, output):
        if target == 0:
            output.append(list(curr_path))
            return

        if target <= 0:
            return

        prev = None
        for i in range(start, len(candidates)):
            if candidates[i] == prev:
                continue

            curr_path.append(candidates[i])

            self.backtrack(candidates, target - candidates[i], i + 1, curr_path, output)

            curr_path.pop()
            prev = candidates[i]

# Time Complexity: O(N*2^N) where N is the length of the candidates array.

# Space Complexity: ?

# Solution: https://www.youtube.com/watch?v=rSA3t6BDDwg