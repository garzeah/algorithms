class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prev_min = prev_max = 1 # Base case
        res = float('-inf')

        # For each number, we want to find the curr_min and curr_max
        # so that it can be used to compute the next numbers
        # curr_min and curr_max
        for num in nums:
            # We want to add num to curr_min and curr_max for cases like [-1, 8]
            # since we'll be left with -8 as the curr_min and curr_max. It would
            # not make sense since the curr_max should be 8 not -8
            curr_min = min(num, prev_min * num, prev_max * num)
            curr_max = max(num, prev_min * num, prev_max * num)
            res = max(res, curr_max)

            # Moving up pointers to compute next curr_min and curr_max
            prev_min, prev_max = curr_min, curr_max

        return res

# Time Complexity: O(n)
# Space Compelxity: O(1)
# Solution: https://www.youtube.com/watch?v=lXVy6YWFcRM