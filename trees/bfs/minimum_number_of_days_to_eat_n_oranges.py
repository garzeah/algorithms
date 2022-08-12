class Solution:
    def minDays(self, n: int) -> int:
        # Think of this problem as a tree in which we start from the root n.
        # At any node, it connects to up to 3 childrens n-1, n // 2 if
        # n % 2 == 0, n // 3 if n % 3 == 0. Then we can level order
        # traverse the tree and find the first occurrence of 0
        # and return its level.
        res = 0
        queue = [n]
        visited = set()

        while queue: #bfs
            day = []

            for num in queue:
                if num == 0:
                    return res

                visited.add(num)

                # Perform all these actions simultaneously and whichever
                # hits 0 first is the minimum number of days
                if num - 1 not in visited:
                    day.append(num - 1)

                if num % 2 == 0 and num // 2 not in visited:
                    day.append(num // 2)

                if num % 3 == 0 and num // 3 not in visited:
                    day.append(num // 3)

            res += 1
            queue = day # Updating day

# Time Complexity: O(logn) since generally we have the possibility
# of cutting our number in half.

# Space Complexity: O(logn)

# Solution: https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/discuss/794172/BFS-with-explanation