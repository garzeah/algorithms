class Solution:
    def trap(self, height: List[int]) -> int:
        left_maxes, right_maxes, min_maxes = [], [], []
        curr_left_max, curr_right_max, total = 0, 0, 0

        # Finding the left max of walls for each position
        for i in range(len(height)):
            curr_left_max = max(curr_left_max, height[i])
            left_maxes.append(curr_left_max)

        # Finding the right max of walls for each position
        for i in reversed(range(len(height))):
            curr_right_max = max(curr_right_max, height[i])
            right_maxes.insert(0, curr_right_max)

        # Finding the min heights of left and right maxes
        for i in range(len(height)):
            min_max = min(left_maxes[i], right_maxes[i])
            min_maxes.append(min_max)

        # Calculating the water height
        for i in range(len(height)):
            min_max, curr_height = min_maxes[i], height[i]
            water_amount = min_max - curr_height # Gives us the current water height

            # Only want values > 0 meaning water is trapped
            if water_amount > 0:
                total += water_amount

        return total

# Time Complexity: O(n^2) can be turned into O(n) with a deque
# Space Complexity: O(n)

