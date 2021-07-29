from heapq import heappush
from heapq import heappop
from collections import deque
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort()
        
        heap = []
        tasks = deque(tasks)
        start,t,i = tasks.popleft()
        res = [i]
        start += t
        
        while tasks or heap:
            while tasks and  tasks[0][0] <= start:
                s,t,i = tasks.popleft()
                heappush(heap, (t, i))
            while heap:
                t, i = heappop(heap)
                res.append(i)
                start += t
                while tasks and  tasks[0][0] <= start:
                    s,t,i = tasks.popleft()
                    heappush(heap, (t, i))
            if not heap and tasks:
                start,t,i = tasks.popleft()
                res.append(i)
                start += t
                while tasks and  tasks[0][0] <= start:
                    s,t,i = tasks.popleft()
                    heappush(heap, (t, i))
                
        
        return res
            
            
        
        
            