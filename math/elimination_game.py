class Solution:
    def lastRemaining(self, n: int) -> int:
        # Moving forward/backwards and keeping
        # track of times n is cut in half
        fwd, k = True, 0
        res = 1 # Starts at 1

        while n > 1:
            # Everytime we have to shift the res (moving forward or
            # n is odd bc if we're moving backwards, we lose the
            # start of the value again) we can we add 2^k to our
            # result to get to where it would have been
            if fwd or n % 2 == 1:
                print(res)
                res += 2 ** k

            k += 1 # Since we're cutting it in half, add to k
            n = n // 2 # Cutting it in half
            fwd = not fwd # Reverse direction

        return res

# Time Complexity: O(log(n))
# Space Complexity: O(1)
# Solution: https://leetcode.com/problems/elimination-game/discuss/87119/JAVA:-Easiest-solution-O(logN)-with-explanation/91915