class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        freq = { 0: -1 } # { key of nums[i] % k: idx }
        prefix_sum = 0

        for (i, num) in enumerate(nums):
            prefix_sum += nums[i]
            # prefix_sum % k, if we encounter this value again then
            # that means we have a subarray that is a multiple of k
            key = prefix_sum % k

            # Record the key and it's index so we can get the length
            if key not in freq:
                freq[key] = i
            # If we encounter it again, then that means we
            # have a subarray sum that is a multiple of k
            elif key in freq:
                if (len(nums[freq[key] + 1: i + 1])) >= 2:
                    return True

        return False

# TC: O(n)
# SC: O(n)
# Solution: https://leetcode.com/problems/continuous-subarray-sum/discuss/1929464/Greatly-Explained-Hashmap-%2B-PrefixSum-in-Python-Time-O(n)-Space-O(min(nk))-Easy-to-Understand!!!