from random import randint
from bisect import bisect_left
from bisect import bisect

class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.dic = defaultdict(list)
        self.arr = arr
        for i, a in enumerate(arr):
            self.dic[a].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        
        for _ in range(20):
            a = self.arr[randint(left, right)]
            lst = self.dic[a]
            l, r = bisect_left(lst, left), bisect(lst, right)
            if r - l >= threshold:
                return a
        return -1
            
            
        


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)