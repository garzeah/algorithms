class Twitter:

    def __init__(self):
        self.timestamp = 0 # Used to track how recent a tweet is
        self.tweet_map = defaultdict(list) # userId -> list of [timestamp, tweetIds] (user's follow list)
        self.follow_map = defaultdict(set) # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.timestamp, tweetId])
        self.timestamp -= 1 # Because we're using a min_heap to get most recent values

    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] # ordered starting from most recent
        min_heap = []

        # A user is technically following themselves so we need to add them
        self.follow_map[userId].add(userId)

        # For every follower a user has, we want to retrieve the 10 most
        # recent tweets and add that list into our min_heap. We'll
        # traverse through each list using the index of each list
        # and its counts in order to achieve this
        for followeeId in self.follow_map[userId]:
            if followeeId in self.tweet_map: # Has at least a tweet
                index = len(self.tweet_map[followeeId]) - 1
                timestamp, tweetId = self.tweet_map[followeeId][index]
                min_heap.append([timestamp, tweetId, followeeId, index - 1])

        heapify(min_heap) # Converting to heap takes O(k)

        while min_heap and len(res) < 10:
            timestamp, tweetId, followeeId, index = heappop(min_heap)
            res.append(tweetId)

            # As long as we can still traverse through the list.
            # Similar to traversing k-sorted lists
            if index >= 0:
                timestamp, tweetId = self.tweet_map[followeeId][index]
                heappush(min_heap, [timestamp, tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

# Time Complexity:
# - getNewsFeed(self, userId): O(n) for the amount of users inside the follow_map.
# O(10*logk) for performing the heap operations leaving us with O(n * log(k))
# where n is the amount of users in the follow_map[userId] and k for getting
# the top 10 most recent posts.

# Solution: https://www.youtube.com/watch?v=pNichitDD2E
