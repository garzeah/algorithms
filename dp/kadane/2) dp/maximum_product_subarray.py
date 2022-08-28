class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # We can use this to keep track of alternative negative
        # values in the event we get an array with negative numbers
        prev_min = prev_max = global_max = nums[0]

        # Because of an edge case where when we have an array of negative numbers
        # it'll yield a sequence of negative and positive numbers. In order to
        # find the maximum values, we need to keep track of the minimum values
        # as they can yield the maximum values.
        for i in range(1, len(nums)):
            curr_min = min(prev_max * nums[i], prev_min * nums[i], nums[i])
            curr_max = max(prev_max * nums[i], prev_min * nums[i], nums[i])
            global_max = max(global_max, curr_max)
            prev_max = curr_max
            prev_min = curr_min

        return global_max

# Time Complexity: O(n)
# Space Compelxity: O(1)
# Solution: https://www.youtube.com/watch?v=lXVy6YWFcRM