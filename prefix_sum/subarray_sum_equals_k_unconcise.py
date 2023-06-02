# Unconcise b/c we're not taking advantage of hash map funcitonality
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {} # prefixSum to freq
        prefixSum, res = 0, 0

        for num in nums:
            prefixSum += num

            # Edge case, for when k = 0
            if prefixSum == k:
                res += 1

            # This means that there exists a number that we have
            # passed that we can add or subtract to reach our k
            if prefixSum - k in freq:
                res += freq[prefixSum - k]

            # Recording the frequencies of the prefix sum
            if prefixSum not in freq:
                freq[prefixSum] = 1
            else:
                freq[prefixSum] += 1

        return res