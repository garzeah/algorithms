class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        nums = sorted(nums, reverse = True)
        nums = sorted(nums, key = lambda x: freq[x])
        return nums

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solution: https://leetcode.com/problems/sort-array-by-increasing-frequency/discuss/1075339/Simple-Python-solution-with-explanation