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

        return self.helper(n, neighbors, -1)

    def helper(self, n, neighbors, start):
        # Run out of numbers to count
        if n == 0:
            return 1

        # Want to get the count of all the possible numbers
        # we can dial that is of size n
        count = 0
        for num in neighbors[start]:
            count += self.helper(n - 1, neighbors, num)

        return count

# Time Complexity: Worst case scenario, I want to say possibly
# O(3^n) because we have at most 3 neighbors to choose from
# when finding digits of size n.

# Space Complexity: Worst case scenario, I want to say possibly
# O(3^n) as well because of each occurrence of recursion in
# our stack.