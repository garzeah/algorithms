class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix, output = [], [], []

        # For each number in an array, we want to get the prefix and postfix
        # sum. Then in order to get the product of array except self, we
        # want to multiply the prefix before the current number with the
        # postfix after the current number

        # Want the value before the first index, since it
        # doesn't exist just use 1 as default
        prefix_sum = 1
        for i in range(len(nums)):
            prefix[i] = prefix_sum
            prefix_sum *= nums[i]

        # Want the value after the last index, since it
        # doesn't exist just use 1 as default
        postfix_sum = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix[i] = postfix_sum
            postfix_sum *= nums[i]

        for i in range(len(nums)):
            output.append(postfix[i] * prefix[len(nums) - 1 - i])

        return output

# Time Complexity: O(n)
# Space Complexity: O(n)