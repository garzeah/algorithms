class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curr_path, output = [], []
        return self.backtrack(n, k, 1, curr_path, output)

    def backtrack(self, n, k, start, curr_path, output):
        if len(curr_path) == k:
            output.append(list(curr_path))
            return

            # From the start to end, we want to find all
            # possible subsets from the index (start) to
            # the numbers right of it to get all subsets
        for i in range(start, n + 1):
            curr_path.append(i)
            self.backtrack(n, k, i + 1, curr_path, output)
            curr_path.pop()

        return output

# Time Complexity: O(K*N^K) because we'll have N choices at each level which will
# double as we go down a level. K will serve as the size of the combination and
# also be the height of our decision tree. Although, N^K is an upper bound. A
# more accurate time would be the k * the formula to find the combination.

# Space Complexity: O(K*N^K) will also serve as an upper bound since
# K will contain the size of the combination and N will serve as
# the amount of elements in our input array. A more tighter
# bound would be the formula to find the combination. As we
# go down a level, we get more values to add.

# Solution: https://www.youtube.com/watch?v=q0s6m7AiM7o