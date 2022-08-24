class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # Sort in-place keep numbers in ascending order
        nums.sort()

        # Counter for valid triplet to make triangle
        valid_triplet = 0

        for i in range(len(nums) - 1, -1, -1):
            first, second, third = 0, i - 1, i

            # Make triplets using basic triangle property a + b > c
            while first < second:
                if nums[first] + nums[second] > nums[third]:
                    valid_triplet += (second - first)
                    # Second edge large enough make it smaller and try next run
                    second -= 1
                else:
                    # First edge is too small make it larger and try next run
                    first += 1

        return valid_triplet

# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Solution: https://leetcode.com/problems/valid-triangle-number/discuss/487683/Python-O(-n2-)-sol.-based-on-sliding-window-and-sorting.-85%2B-With-explanation