class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum, res = 0, 0
        # Adding a base case of 0 in the event curr_sum - k = 0
        prefix_sums = { 0: 1 } # Prefix sum : amount of ways to get to our prefix sum

        # The main idea behind this is whenever curr_sum has increased by
        # a value of k, then we've found a subarray that is equal to k
        for num in nums:
            curr_sum += num
            # If a difference exists then curr_sum has increased by
            # a value of k, so we can add that to our result
            res += prefix_sums.get(curr_sum - k, 0)
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1 #

        return res

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solution 1: https://www.youtube.com/watch?v=fFVZt-6sgyo
# Solution 2: https://leetcode.com/problems/subarray-sum-equals-k/discuss/341399/Python-clear-explanation-with-code-and-example