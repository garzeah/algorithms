class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Why greedy?
        # If we were to take the difference of city b and a,
        # we could use that to determine the minimum costs
        # since this tells us how much we would save going
        # to city a instead of b

        # In order to find the minimum cost, a way we can approach
        # this is to find the difference between city b and city a
        # and then sort it, and grab the first n values for city b
        # in calculating minimum costs
        diffs = []
        for a, b in costs:
            # Tells us how much we would save going to city b than a
            # If it is negative, we would save that amount
            # If it is positive, we would lose that amount
            diffs.append([b - a, a, b])

        diffs.sort()

        # Grabbing the first n values for city b since we wouldn't
        # save that much going to city a since it is sorted which
        # is why we we grab the first n values for city b
        res = 0
        for i in range(len(diffs)):
            if i < len(diffs) // 2:
                res += diffs[i][2]
            else:
                res += diffs[i][1]

        return res

# Time Complexity: O(nlogn)
# Space Complexity: O(n)
# Solution: https://www.youtube.com/watch?v=d-B_gk_gJtQ
