from sortedcontainers import SortedList
from bisect import bisect_left

class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        size = sorted([[num, id] for id, num in rooms])
        q = sorted([(num, id, i) for i,(id, num) in enumerate(queries)])[::-1]
        n, m = len(rooms), len(queries)
        lst = SortedList()
        ans = [-1] * m
        #print(size, q)
        p2 = n
        for num, id, i in q:
            j = bisect_left(size, [num])
            
            
            for k in range(j, p2):
                lst.add(size[k][1])
            p2 = j
            if not lst:
                continue
            x = bisect_left(lst, id)
            #print(lst, id, x)
            if  x == len(lst) or (x != 0 and id - lst[x-1] <= lst[x] -id):
                ans[i] = lst[x - 1]
            else:
                ans[i] = lst[x]
        
        return ans
        
        