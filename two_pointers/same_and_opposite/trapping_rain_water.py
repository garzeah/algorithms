class Solution:
    def trap(self, height: List[int]) -> int:
        if height is None:
            return 0

        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        output = 0

        # We want to shift the smaller value first whether that
        # be left_max or right_max. We want to get the minimum
        # of left and right for its current positions then we
        # can use that to get the height which is
        # min(l, r) - height[l or r]
        while l < r:
            if left_max <= right_max:
                l += 1
                left_max = max(left_max, height[l])
                output += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                output += right_max - height[r]

        return output

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solution: https://www.youtube.com/watch?v=ZI2z5pq0TqA