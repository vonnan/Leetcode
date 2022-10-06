from bisect import bisect

class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)
        self.time = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append(timestamp)
        self.time[timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect(self.dic[key], timestamp) - 1
        
        if idx == -1:
            return ""
        return self.time[self.dic[key][idx]]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)