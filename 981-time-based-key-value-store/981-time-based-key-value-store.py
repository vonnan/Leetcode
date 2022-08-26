from bisect import bisect

class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)
        self.time = defaultdict(int)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append(timestamp)
        self.time[timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        lst = self.dic[key]
        idx = bisect(lst, timestamp)
        if idx == 0:
            return ""
        return self.time[lst[idx - 1]]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)