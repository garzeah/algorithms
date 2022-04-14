class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curr_path, output = [], []
        self.backtrack(n, k, 1, curr_path, output)
        return output

    def backtrack(self, n, k, index, curr_path, output):
        if len(curr_path) == k:
            output.append(list(curr_path))
            return

        # For each level, we want to add all the numbers
        # from 1 to n for each of our current paths
        for i in range(index, n + 1):
            curr_path.append(i)
            self.backtrack(n, k, i + 1, curr_path, output)
            # Want to remove the value we added for the next sibling
            curr_path.pop()

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