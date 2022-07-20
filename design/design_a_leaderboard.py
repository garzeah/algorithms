class Leaderboard:

    def __init__(self):
        self.score = {}

    # Time Complexity: O(1)
    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.score:
            self.score[playerId] = 0

        self.score[playerId] += score

    # Time Complexity: O(nlogk) where n is the amount of players and k is the
    # amount of players
    def top(self, K: int) -> int:
        max_heap = []
        res = 0

        for player, score in self.score.items():
            heappush(max_heap, -score)

        i = 0
        while max_heap and i < K:
            res += heappop(max_heap)
            i += 1

        return -res

    # Time Complexity: O(1)
    def reset(self, playerId: int) -> None:
        self.score[playerId] = 0

# Space Complexity: O(n) where n is the amount of players


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)