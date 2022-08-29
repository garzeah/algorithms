class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Want to record the a number and the indices they
        # appear in, as well as the max_degree and
        # min_length of our contiguous subarray
        nums_map, max_deg, min_len = defaultdict(list), 0, float('inf')
        for (i, num) in enumerate(nums):
            nums_map[num].append(i)
            max_deg = max(max_deg, len(nums_map[num]))

        # Find an indices that equal our max_degree
        # then record the smallest subarray
        for (num, indices) in nums_map.items():
            if max_deg == len(indices):
                min_len = min(min_len, indices[-1] - indices[0] + 1)

        return min_len

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solution: https://leetcode.com/problems/degree-of-an-array/discuss/108647/Python-O(n)-concise-with-explanation-(two-approaches)