class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # We can use total to keep track of the prefixSum of 0s and 1s
        # If we encounter a 0/1 we will decrement/increment the total
        # value. If it equals 0, we have found a new subarray that
        # has the maxLength
        total, maxLength = 0, 0
        prefixSum = {} # prefixSum : index

        for (i, num) in enumerate(nums):
            if num == 0:
                total -= 1
            else:
                total += 1

            # Edge case, so whenever we have a count of zero that means
            # we encountered a new subarray that has the maxLength
            if total == 0:
                maxLength = i + 1

            # We want to record the index of the current prefixSum
            if total not in prefixSum:
                prefixSum[total] = i
            # We have encountered this prefixSum before meaning
            # that we can subtract the current index with the
            # last recorded index to get the current length
            else:
                maxLength = max(maxLength, i - prefixSum[total])

        return maxLength

# TC: O(n)
# SC: O(n)
# Solution: https://leetcode.com/problems/contiguous-array/discuss/1743720/Python-Javascript-Easy-solution-with-very-clear-Explanation