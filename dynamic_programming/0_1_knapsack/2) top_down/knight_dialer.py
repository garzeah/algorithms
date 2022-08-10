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

        return self.helper(n, neighbors, -1, {}) % (10 ** 9 + 7)

    def helper(self, n, neighbors, start, cache):
        if (n, start) in cache:
            return cache[(n, start)]

        # Run out of numbers to count
        if n == 0:
            return 1

        # Want to get the count of all the possible numbers
        # we can dial that is of size n
        count = 0
        for num in neighbors[start]:
            count += self.helper(n - 1, neighbors, num, cache)

        # Cache values so we don't have to recompute
        cache[(n, start)] = count

        return count

# Time Complexity: O(n) because since we cached everything, we
# do not have to recompute the previous values

# Space Complexity: O(n) because of the stack space in recursion