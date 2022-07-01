from bisect import bisect_left
from bisect import bisect

class LogSystem:

    def __init__(self):
        self.format = {x: i+ 2 for i, x in enumerate("Year:Month:Day:Hour:Minute:Second".split(":"))}
        self.dic = defaultdict(int)

    def put(self, id: int, timestamp: str) -> None:
        self.dic[int(timestamp.replace(":", ""))] = id
        

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        start, end = start.replace(":", ""), end.replace(":", "")
        idx = 2 * self.format[granularity]
        start = int(start[:idx] + "0"*(14-idx))
        end = int(end[:idx] + "59"* (7 - idx//2))
        #print(idx, start, end, self.dic)
        return [val  for key, val in self.dic.items() if start <= key <= end]
            
            
        


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)