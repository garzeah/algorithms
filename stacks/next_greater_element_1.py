class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1Idx = { num: i for (i, num) in enumerate(nums1) }
        res = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            curr = nums2[i]

            # Want to maintain a monotonic decreasing stack bc whenever
            # we encounter a value that breaks this then that means we
            # found the next greater elem. and we want to update the
            # values in that correspond with nums1 with our res
            while stack and curr > stack[-1]:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = curr

            # Only want numbers that are in nums1
            if curr in nums1Idx:
                stack.append(curr)

        return res

# Time Complexity: O(n + m) where n is length of nums1 and m is length of nums2
# Space Comlexity: O(n) because we only store the size of nums1 in our stack
# and hash map.
# Solution: https://www.youtube.com/watch?v=68a1Dc_qVq4