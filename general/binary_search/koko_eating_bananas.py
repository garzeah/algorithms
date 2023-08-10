class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Min and max rates that Koko can eat a pile of bananas
        start, end = 1, max(piles)
        k = 0 # rate

        while start <= end:
            mid = (start + end) // 2

            # Calculating the total hours it takes to eat all piles
            hours = 0
            for pile in piles:
                hours += ceil(pile / mid)

            # Record the min hour where she can
            # eat all bananas within h hours
            if hours <= h:
                k = mid
                end = mid - 1
            else:
                start = mid + 1

        return k

# Time Complexity: O(log(n) * m) where n is the length of all
# possibles rates and m is the length of piles.

# Space Complexity: O(1)

# Solution: https://www.youtube.com/watch?v=U2SozAs9RzA