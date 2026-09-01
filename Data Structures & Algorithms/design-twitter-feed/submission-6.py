class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.posts = defaultdict(list)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.time, tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        offset = {}
        if self.posts[userId]:
            offset[userId] = len(self.posts[userId]) - 1
        for followee in self.following[userId]:
            if self.posts[followee]:
                offset[followee] = len(self.posts[followee]) - 1
        # initialize heap with one post from each poster
        heap = []
        for poster in offset:
            time, post = self.posts[poster][offset[poster]]
            heapq.heappush(heap, (-1*time, post, poster))
        feed = []
        while heap and len(feed) < 10:
            _, post, poster = heapq.heappop(heap)
            feed.append(post)
            offset[poster] -= 1
            if offset[poster] > -1:
                time, post = self.posts[poster][offset[poster]]
                heapq.heappush(heap, (-1*time, post, poster))
        return feed      

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
