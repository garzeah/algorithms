class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l, r = 0, len(people) - 1
        people.sort()
        boats = 0

        while l <= r:
            # We can fit 2 people on this boat
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            # Since it is sorted and r is <= limit, we can
            # decrement and add an additional boat
            else:
                r -= 1

            boats += 1

        return boats

# Time Complexity: O(nlogn)
# Space Complexity: O(1)
# Solution: https://leetcode.com/problems/boats-to-save-people/discuss/1878155/Explained-Python-2-Pointers-Solution