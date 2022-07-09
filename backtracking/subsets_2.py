class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        curr_path, res = [], []
        return self.backtrack(sorted(nums), 0, curr_path, res)

    def backtrack(self, nums, start, curr_path, res):
        res.append(list(curr_path))


        for i in range(start, len(nums)):
            # "i > start" signifies paths that we haven't
            # visited yet. If i and start are equal then
            # we haven't visited it yet. If i is > than
            # start then we already have visited it
            if i > start and nums[i - 1] == nums[i]:
                continue

            # Decision to include nums[i] and not include nums[i]
            curr_path.append(nums[i])
            self.backtrack(nums, i + 1, curr_path, res)
            curr_path.pop()

        return res

# Time Complexity: Since, in each step, the number of subsets doubles (if not duplicate) as
# we add each element to all the existing subsets, therefore, we will have a total of
# O(2^N) subsets, where ‘N’ is the total number of elements in the input set. And
# since we construct a new subset from an existing set, therefore, the time
# complexity of the above algorithm will be O(N*2^N).

# Space Complexity: All the additional space used by our algorithm is for the res list.
# Since, at most, we will have a total of O(2^N) subsets, and each subset can take up to
# O(N) space, therefore, the space complexity of our algorithm will be O(N*2^N).