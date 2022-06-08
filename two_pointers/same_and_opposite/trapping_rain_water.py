class Solution:
    def trap(self, height: List[int]) -> int:
        if height is None:
            return 0

        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        output = 0

        # We want to shift the smaller max value first. Left
        # and right pointers do not depend on each other bc
        # we want the minimum of left and right and as long
        # as left is smaller we will not need the other max
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