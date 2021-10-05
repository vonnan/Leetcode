from bisect import bisect
from bisect import insort

class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        lst = []
        for day, v in enumerate(bulbs):
            idx = bisect(lst, v)
            if lst:
                
                if idx == 0:
                    if lst[0] - v == k+1:
                        return day + 1
                elif idx == len(lst):
                    if v - lst[-1] == k + 1:
                        return day + 1
                elif lst[idx] - v == k + 1 or (v - lst[idx-1] == k + 1):
                    return day + 1
            lst.insert(idx, v)
        return -1
                