class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        # p*s = q*r
        # p = length of walls
        # s = number of stacked boxes
        # q = laser meets wall at distance q
        # r = number of reflecting times

        # Reduce 2 from the equation since it can be simplified
        while p % 2 == 0 and q % 2 == 0:
            p = p / 2
            q = q / 2

        # If p is even then q is odd b/c of p*s = q*r since r will be
        # even which means that the ray ends at the top left corner
        if p % 2 == 0:
            return 2

        # If q is even then that means p is odd b/c of p*s = q*r since s
        # will be even which means that the ray ends at the top right corner
        if q % 2 == 0:
            return 0

        return 1

# Time Complexity: O(min(log(p), log(q)) since we're cutting it in half
# Space Complexity: O(1)
# Solution: https://leetcode.com/problems/mirror-reflection/discuss/2377070/Pseudocode-Explain-Why-Odd-and-Even-Matter