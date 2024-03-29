class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums) # Using a counter to prevent dupes
        curr_path, res = [], []
        return self.backtrack(sorted(nums), count, curr_path, res)

    def backtrack(self, nums, count, curr_path, res):
        if len(curr_path) == len(nums):
            res.append(list(curr_path))
            return

        for key in count:
            # When it reaches 0, it'll prevent dupes since we
            # don't have any more counts to use for current key
            if count[key] > 0:
                curr_path.append(key)
                count[key] -= 1

                self.backtrack(nums, count, curr_path, res)

                count[key] += 1
                curr_path.pop()

        return res

# Time Complexity: We know that there can be a total of N! permutations of a set with
# ‘N’ numbers. We are also iterating through our counter for each path which is O(N)
# (where N is every unique number in our input arrays) which makes the overall time
# complexity of our algorithm O(N*N!).

# Space Complexity: There are a total of N! permutations with N being the length of
# unique elements. Since we have to create a list for each permutation, the space
# complexity will be O(N*N!)

# Solution: https://www.youtube.com/watch?v=qhBVWf0YafA