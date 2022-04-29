class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr_path, output = [], []
        return self.backtrack(sorted(nums), 0, curr_path, output)

    def backtrack(self, nums, start, curr_path, output):
        output.append(list(curr_path))

        for i in range(start, len(nums)):
            # From the start to end, we want to find all
            # possible subsets from the index (start) to
            # the numbers right of it to get all subsets
            curr_path.append(nums[i])
            self.backtrack(nums, i + 1, curr_path, output)
            curr_path.pop()

        return output

# Time Complexity: Since, in each step, the number of subsets doubles (if not duplicate) as
# we add each element to all the existing subsets, therefore, we will have a total of
# O(2^N) subsets, where ‘N’ is the total number of elements in the input set. And
# since we construct a new subset from an existing set, therefore, the time
# complexity of the above algorithm will be O(N*2^N).

# Space Complexity: All the additional space used by our algorithm is for the output list.
# Since, at most, we will have a total of O(2^N) subsets, and each subset can take up to
# O(N) space, therefore, the space complexity of our algorithm will be O(N*2^N).