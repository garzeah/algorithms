class Twitter:

    def __init__(self):
        self.count = 0 # Used to figure out most recent tweet
        self.tweet_map = defaultdict(list) # userId -> list of [count, tweetIds]
        self.follow_map = defaultdict(set) # userId -> set of followeeId


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.count, tweetId])
        self.count -= 1 # For our min_heap


    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] # Ordered starting from recent
        min_heap = []

        self.follow_map[userId].add(userId) # Since it factors user following himself

        # Want the most recent tweet
        for followeeId in self.follow_map[userId]:
            # Checking if we have a tweet
            if followeeId in self.tweet_map:
                index = len(self.tweet_map[followeeId]) - 1
                count, tweetId = self.tweet_map[followeeId][index]
                # Want to get next tweet from this followeeId
                heappush(min_heap, [count, tweetId, followeeId, index - 1])

        # Getting 10 most recent tweets
        while min_heap and len(res) < 10:
            count, tweetId, followeeId, index = heappop(min_heap)
            res.append(tweetId)

            # As long as there are still elements...
            if index >= 0:
                count, tweetId = self.tweet_map[followeeId][index]
                heappush(min_heap, [count, tweetId, followeeId, index - 1])

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Checking if they are following first
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

# Time Complexity: O(k * logk) where k is the number of tweet_maps
# pairs we access when accessing the news feed.

# Space Complexity: O(n x m) where n is the amount unique ids
# and m is the max length of the list.