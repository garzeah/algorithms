class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # The map returns the index where the sum of every element up
        # to that index from index 0 is prefix_sum - k. If we have a
        # prefix_sum - k in our map, then that means the elements
        # between the indexes incremented the total sum by k
        sum_to_idx = { 0: -1 } # prefix_sum to idx map
        prefix_sum, max_length = 0, 0

        for (i, num) in enumerate(nums):
            prefix_sum += num

            # There are only 2 cases when we can update max_length
            # Case 1: Prefix sum is k
            # Case 2: Prefix sum is different from k, but we can truncate a prefix of the array
            if prefix_sum == k:
                max_length = max(max_length, i + 1)
            elif prefix_sum - k in sum_to_idx:
                max_length = max(max_length, i - sum_to_idx[prefix_sum - k])

            # Store prefix sum in dictionary, only if it is not seen because
            # only the earlier (thus shorter) subarray is valuable, when we
            # want to get the max_len after truncation
            if prefix_sum not in sum_to_idx:
                sum_to_idx[prefix_sum] = i

        return max_length

# TC: O(n)
# SC: O(n)
# Solution: https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/discuss/77784/O(n)-clean-short-JavaPython-solution-with-HashMap-(with-code-comments)