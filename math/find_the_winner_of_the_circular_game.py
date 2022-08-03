class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [i for i in range(1, n+1)]
        start = 0 # Starting with the first element

        while len(players) > 1:
            pop_element = (start + k - 1) % n # Find where we need to remove elment
            players.pop(pop_element) # Removing the element
            n -= 1 # Updating the size
            start = pop_element % n # Updating the next starting element since size was changed

        return players[0]

# Time Complexity: O(n^2)
# Space Complexity: O(n)
# Solution: https://leetcode.com/problems/find-the-winner-of-the-circular-game/discuss/2254227/PYTHON-oror-EASY-APPROACH-oror-BEATS-98.77