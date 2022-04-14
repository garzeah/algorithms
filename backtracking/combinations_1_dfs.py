class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curr_comb, output = [], []
        self.dfs(n, k, 1, curr_comb, output)
        return output

    def dfs(self, n, k, index, curr_comb, output):
        # When our current combination is equal to k
        # we can add it to our output
        if len(curr_comb) == k:
            output.append(list(curr_comb))
            return

        for i in range(index, n + 1):
            curr_comb.append(i)
            self.dfs(n, k, i + 1, curr_comb, output)
            # Want to remove the value we just added before
            # adding in the next number
            curr_comb.pop()

# Time Complexity: O(K*N^K) because we'll have N choices at each level which will
# double as we go down a level. K will serve as the size of the combination and
# also be the height of our decision tree. Although, N^K is an upper bound. A
# more accurate time would be the k * the formula to find the combination.

# Space Complexity: O(N^K) will also serve as an upper bound since
# K will contain the size of the combination and N will serve as
# the amount of numbers we need to find a combination of. A more
# tighter bound would be the formula to find the combination.