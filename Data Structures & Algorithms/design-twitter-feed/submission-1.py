class Twitter:

    def __init__(self):
        self.global_feed = []
        self.following = defaultdict(set) # userID to set of users
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.global_feed.append((userId, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        posts_count = 0
        for i in range(len(self.global_feed) - 1, -1, -1):
            poster = self.global_feed[i][0]
            if poster in self.following[userId] or poster == userId:
                res.append(self.global_feed[i][1])
                posts_count += 1
            if posts_count == 10:
                break
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

        
