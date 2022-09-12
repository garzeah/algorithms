class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        dates = []

        # For every birth and death year, we'll pair it with a tuple
        # indicating that a person is existing at that time. Then
        # we can sort it and get the max earliest year when
        # iterating through the results
        for birth, death in logs:
            dates.append((birth, 1))
            dates.append((death, -1))

        dates.sort()

        local_pop = max_pop = res = 0
        for year, pop in dates:
            local_pop += pop
            if local_pop > max_pop:
                max_pop = max(max_pop, local_pop)
                res = year

        return res

# Time Complexity: O(nlogn)
# Space Complexity: O(n)
# Solution: https://leetcode.com/problems/maximum-population-year/discuss/1199494/Python-sorting-max-overlapping-segments-algorithm