class Solution:
    def trap(self, height: List[int]) -> int:
        if height is None:
            return 0

        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        res = 0

        # We can get the amount of trapped rainwater by subtracting the
        # min(max(left_max, height[l]), max(right_max, height[r])) aka
        # (the min wall of both the left and right maxes) with the current
        # height. In order to do this using two pointers, we can get the
        # minimum as long as maintain left_max <= right_max when traversing
        # through the array.
        while l < r:
            if left_max <= right_max:
                l += 1
                left_max = max(left_max, height[l])
                res += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                res += right_max - height[r]

        return res

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solution: https://www.youtube.com/watch?v=ZI2z5pq0TqA