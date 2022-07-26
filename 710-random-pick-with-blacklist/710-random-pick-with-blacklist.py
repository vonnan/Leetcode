from random import randint
from bisect import bisect_left
class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.dic = {num : - 1 for num in blacklist}
        self.m = n - len(self.dic)
        i = n - 1
        for num in self.dic:
            while i in self.dic:
                i -= 1
            if num < self.m:
                self.dic[num] = i
                i -= 1
        

    def pick(self) -> int:
        num = randint(0, self.m - 1)
        if num in self.dic:
            return self.dic[num]
        return num
            
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()