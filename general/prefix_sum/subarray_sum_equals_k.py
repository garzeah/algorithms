class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum, res = 0, 0
        prefix_sums = { 0: 1 } # Base case of 0?

        # The main idea behind this is whenever curr_sum has increased by
        # a value of k, then we've found a subarray that is equal to k
        for num in nums:
            curr_sum += num # Building up the current prefix sum
            curr_diff = curr_sum - k # Getting the current difference
            res += prefix_sums.get(curr_diff, 0) # Checking if there is an increase by k
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1 #

        return res

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solution 1: https://www.youtube.com/watch?v=fFVZt-6sgyo
# Solution 2: https://leetcode.com/problems/subarray-sum-equals-k/discuss/341399/Python-clear-explanation-with-code-and-example