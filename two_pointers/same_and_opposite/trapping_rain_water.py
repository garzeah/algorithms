class Solution:
    def trap(self, height: List[int]) -> int:
        if height is None:
            return 0

        res, l, r = 0, 0, len(height) - 1
        l_max, r_max = height[l], height[r]

        # In order to find how much water we can trap at height[i],
        # we need to know the max left and right height of every
        # single position then take the min(left[i], right[i])
        # and subtract it with height[i].

        # However, we can optimize this by using pointers by keeping
        # track of l_max and r_max. As long as l_max <= r_max we are
        # getting the min(l_max, r_max).
        while l < r:
            if l_max <= r_max:
                l += 1
                l_max = max(l_max, height[l])
                res += l_max - height[l] # Counting after sliding bc we cant trap water at edges
            else:
                r -= 1
                r_max = max(r_max, height[r])
                res += r_max - height[r] # Counting after sliding bc we cant trap water at edges

        return res

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solution: https://www.youtube.com/watch?v=ZI2z5pq0TqA