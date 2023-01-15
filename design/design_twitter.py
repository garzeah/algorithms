class Twitter:

    def __init__(self):
        self.timestamp = 0 # Used to track how recent a tweet is
        self.tweets = defaultdict(list) # userId -> list of [timestamp, tweetIds] (user's follow list)
        self.following = defaultdict(set) # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.timestamp, tweetId])
        self.timestamp -= 1 # Because we're using a max_heap to get most recent values

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []

        # A user is technically following themselves so we need to add them
        self.following[userId].add(userId)

        # For every follower a user has, we want to retrieve the 10 most
        # recent tweets and add that list into our max_heap. We'll
        # traverse through each list using the index of each list
        # and its counts in order to achieve this
        for followeeId in self.following[userId]:
            if followeeId in self.tweets: # Has at least a tweet
                index = len(self.tweets[followeeId]) - 1
                timestamp, tweetId = self.tweets[followeeId][index]
                heappush.append(max_heap, [timestamp, tweetId, followeeId, index - 1])

        res = [] # ordered starting from most recent
        while max_heap and len(res) < 10:
            timestamp, tweetId, followeeId, index = heappop(max_heap)
            res.append(tweetId)

            # As long as we can still traverse through the list.
            # Similar to traversing k-sorted lists
            if index >= 0:
                timestamp, tweetId = self.tweets[followeeId][index]
                heappush(max_heap, [timestamp, tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

# Time Complexity:
# - getNewsFeed(self, userId): O(n) for the amount of users inside the following.
# O(10*logk) for performing the max_heap operations leaving us with O(n * log(k))
# where n is the amount of users in the following[userId] and k for getting
# the top 10 most recent posts.

# Solution: https://www.youtube.com/watch?v=pNichitDD2E
