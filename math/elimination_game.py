class Solution:
    def lastRemaining(self, n: int) -> int:
        fwd = True # flag for forward/backward elimination
        step = 2 # elimination step/interval
        res = 1 # elimination "pointer" will start at 1 bc of range

        while n > 1:
            # Want to remove the first number in our elimination pointer
            if fwd or n % 2 == 1:
                # When moving forward or if odd, we have to recalculate
                # our result since we're removing the starting values
                res += step // 2 # Moving head to the next "position" by adding 2^kth rounds (k starts at 0)

            step *= 2 # Adding a step in order to get the kth round
            n = n // 2 # Cutting size in half
            fwd = not fwd # Reverse the pass direction

        return res

# Time Complexity: O(log(n))
# Space Complexity: O(1)
# Solution: https://leetcode.com/problems/elimination-game/discuss/87119/JAVA:-Easiest-solution-O(logN)-with-explanation/91915