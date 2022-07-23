
from bisect import bisect_left
from bisect import insort
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        lst = []
        res = []
        
        for num in nums[::-1]:
            if not lst:
                lst = [num]
                res = [0]
            else:
                idx = bisect_left(lst, num)
                lst.insert(idx, num)
                res.append(idx)
        
        return res[::-1]
            
        
        