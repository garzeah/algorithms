class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []

        # Base Case
        if len(nums) == 1:
            return [list(nums)]

        # Recursive Case
        for i in range(len(nums)):
            num = nums.pop(0)
            perms = self.permute(nums)

            # Append the values we just removed
            for perm in perms:
                perm.append(num)

            # Extend iterates over its elements and adds
            # each element to the list and extending it
            output.extend(perms)
            nums.append(num)

        return output

# Time Complexity: O(N * N!) where N is the amount of elements
# we have in our array.

# Space Complexity: O(N * N!) since N! will be the amount of
# arrays we'll have and in each of them we'll have N elements.

# Solution: https://www.youtube.com/watch?v=s7AvT7cGdSo