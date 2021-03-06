from collections import Counter
from collections import deque
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.queue = deque([])
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.queue.append(timestamp)
               

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while self.queue and self.queue[0] <=  timestamp-300:
            self.queue.popleft()
        
        return len(self.queue)
            
            
        
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)