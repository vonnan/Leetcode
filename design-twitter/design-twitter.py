from collections import defaultdict
from heapq import merge
from heapq import heappush
from heapq import heappop

from itertools import islice

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ts = 0
        self.post = defaultdict(deque)
        self.follower = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.ts -= 1
        self.post[userId].appendleft((self.ts, tweetId))
        if len(self.post) > 10:
            self.post.pop()
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        heap = []
        for ts, tweetId in self.post[userId]:
            heappush(heap, (ts, tweetId))
        if userId in self.follower:
            for followee in self.follower[userId]:
                for ts, tweetId in self.post[followee]:
                    heappush(heap, (ts, tweetId))
        res = []
        for _ in range(10):
            if heap:
                ts, tweetId = heappop(heap)
                res.append(tweetId)
            else:
                break
        return res
        """
        
        candidates = (self.post[u] for u in (self.follower[userId] | {userId}))
        merged_list = heapq.merge(*candidates)
        return [val for ts, val in list(merged_list)[:10]]

           

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follower[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follower[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)