class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        curr_perm, output = [], []
        self.bfs(nums, 0, curr_perm, output)
        return output


    def bfs(self, nums, index, curr_perm, output):
        if index == len(nums):
            output.append(curr_perm)
        else:
            # Create a new permutation by adding the current number at every position
            for i in range(len(curr_perm) + 1):
                new_perm = list(curr_perm)
                new_perm.insert(i, nums[index])
                self.bfs(nums, index + 1, new_perm, output)

# Time Complexity: O(N * N!) where N is the total amount numbers in our element.

# Space Complexity: O(N * N!) where N is the total amount of numbers in our array.

# Solution: https://www.educative.io/courses/grokking-the-coding-interview/B8R83jyN3KY