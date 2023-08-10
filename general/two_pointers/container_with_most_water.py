class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, result = 0, len(height) - 1, 0

        while left < right:
            # Calculate minimum length between 2 values so water does not overflow
            minHeight = min(height[left], height[right])
            width = right - left # Calculating the distance from right to left

            result = max(result, minHeight * width)

            # Calculating the max area with each iteration
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result

# Time Complexity: O(n)
# Space Complexity: O(1)