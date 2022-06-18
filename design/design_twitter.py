class Twitter:

    def __init__(self):
        self.count = 0 # Used to track how recent a tweet is
        self.tweet_map = defaultdict(list) # user_id -> list of [count, tweetIds]
        self.follower_map = defaultdict(set) # user_id -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] # ordered starting from most recent
        min_heap = []

        # A user is technically following themselves so we need to add them
        self.follower_map[userId].add(userId)

        # For every follower a user has, we want to retrieve the 10 most
        # recent tweets and add that list into our min_heap. We'll
        # traverse through each list using the index of each list
        # and its counts in order to achieve this
        for followeeId in self.follower_map[userId]:
            if followeeId in self.tweet_map: # Has at least a tweet
                index = len(self.tweet_map[followeeId]) - 1
                count, tweetId = self.tweet_map[followeeId][index]
                min_heap.append([count, tweetId, followeeId, index - 1])

        heapify(min_heap) # Converting to heap takes O(k)

        while min_heap and len(res) < 10:
            count, tweetId, followeeId, index = heappop(min_heap)
            res.append(tweetId)

            # As long as we can still traverse through the list.
            # Similar to traversing k-sorted lists
            if index >= 0:
                count, tweetId = self.tweet_map[followeeId][index]
                heappush(min_heap, [count, tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower_map[followerId]:
            self.follower_map[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

# Time Complexity:
# - getNewsFeed(self, userId): O(k) since we are using heapify. If we were to use
# an array it would be a similar time comeplexity O(10*k). However, if we were
# able to choose how many most recent tweets we want then using a heap would
# be better in terms of time complexity.

# Solution: https://www.youtube.com/watch?v=pNichitDD2E