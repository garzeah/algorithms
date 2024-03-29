class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        curr_path, res = [], []
        return self.backtrack(nums, curr_path, res)

    def backtrack(self, nums, curr_path, res):
        if len(curr_path) == len(nums):
            res.append(list(curr_path))
            return

        for i in range(len(nums)):
            # If number is in our current permutation, don't add it
            if nums[i] in curr_path:
                continue

            # Otherwise, if it is not in our current permutation, add it
            curr_path.append(nums[i])
            self.backtrack(nums, curr_path, res)
            curr_path.pop()

        return res

# Time Complexity: We know that there are a total of N! permutations of a set with
# ‘N’ numbers. We are also interating through nums for each path which is O(N),
# which makes the overall time complexity of our algorithm O(N*N!).

# Space Complexity: There are a total of N! permutations with N being the length of
# the elements. Since we have to create a list for each permutation, the space
# complexity will be O(N*N!)