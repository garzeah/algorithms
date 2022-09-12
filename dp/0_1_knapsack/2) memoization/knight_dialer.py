class Solution:
    def knightDialer(self, n: int) -> int:
        neighbors = {
            -1: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
            1: (6, 8),
            2: (7, 9),
            3: (4, 8),
            4: (3, 9, 0),
            5: tuple(), # 5 has no neighbors
            6: (1, 7, 0),
            7: (2, 6),
            8: (1, 3),
            9: (2, 4),
            0: (4, 6),
        }

        dp = [[-1 for x in range(n + 1)] for y in range(len(neighbors))]
        return self.helper(n, neighbors, -1, dp) % (10 ** 9 + 7)

    def helper(self, target, neighbors, i, dp):
        # Run out of numbers to count
        if target == 0:
            return 1

        # Want to get the count of all the possible numbers
        # we can dial that is of size n
        if dp[i][target] == -1:
            count = 0
            for nei in neighbors[i]:
                count += self.helper(target - 1, neighbors, nei, dp)

            # Cache values so we don't have to recompute
            dp[i][target] = count

        return dp[i][target]

# Time Complexity: O(n*m) because since we cached everything, we
# do not have to recompute the previous values

# Space Complexity: O(n*m) because of the stack space in recursion

# Solution: https://leetcode.com/problems/knight-dialer/discuss/1476546/Python-Simple-Recursion-%2B-Memoization