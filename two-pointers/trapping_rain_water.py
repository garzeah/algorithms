class Solution:
    def trap(self, height: List[int]) -> int:
        leftMaxes, rightMaxes, minWallHeights = [], [], []
        currLeftMax, currRightMax, total = 0, 0, 0

        # Finding the left max of walls for each position
        for i in range(len(height)):
            currLeftMax = max(currLeftMax, height[i])
            leftMaxes.append(currLeftMax)

        # Finding the right max of walls for each position
        for i in reversed(range(len(height))):
            currRightMax = max(currRightMax, height[i])
            rightMaxes.insert(0, currRightMax)

        # Finding the min wall heights of left and right maxes
        for i in range(len(height)):
            minWallHeight = min(leftMaxes[i], rightMaxes[i])
            minWallHeights.append(minWallHeight)

        # Calculating the water height
        for i in range(len(height)):
            currHeight = height[i]
            currMinWallHeight = minWallHeights[i]

            # Gives us the current water height
            currWaterHeight = currMinWallHeight - currHeight

            # Only want values > 0 meaning water is trapped
            if currWaterHeight > 0:
                total += currWaterHeight


        return total

# Time Complexity: O(n^2) can be turned into O(n) with a deque
# Space Complexity: O(n)

