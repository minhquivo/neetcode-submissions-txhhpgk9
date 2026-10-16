class Twitter:

    def __init__(self):
        self.following_map = defaultdict(set)
        self.post_map = defaultdict(list)
        self.time = 0 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.post_map[userId].append([self.time, tweetId])
        self.time += 1 

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = [] 
        heapq.heapify_max(maxHeap)

        for time, tweetId in self.post_map[userId]: 
            heapq.heappush_max(maxHeap, [time, tweetId]) 

        for following in self.following_map[userId]: 
            for time, tweetId in self.post_map[following]: 
                heapq.heappush_max(maxHeap, [time, tweetId]) 

        res = [] 
        for i in range(10): 
            if maxHeap: 
                res.append(heapq.heappop_max(maxHeap)[1])

        return res  

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following_map[followerId]:
            self.following_map[followerId].remove(followeeId)
