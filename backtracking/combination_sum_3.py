class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        output = []
        return self.backtrack(k, n, 1, [], output)

    def backtrack(self, k, target, digit, start, curr_path, output):
        if target < 0:
            return

        # Want to make sure target matches and digit is unique
        if target == 0 and len(curr_path) == k:
            output.append(list(curr_path))
            return

        # From the start to end, we want to find all possible
        # unique combinations that equal our target
        for i in range(start, 10):
            curr_path.append(i)
            self.backtrack(k, target - i, i + 1, curr_path, output)
            curr_path.pop()

        return output

# Time Complexity: O(N*2^N) where N is the target value since at most our
# decision tree can reach a height of t with the levels either growing
# or getting smaller.

# Space Complexity: ?