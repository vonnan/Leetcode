class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks = sorted(tasks, key= lambda x: (x[0]-x[1], -x[1]))
        tot = sum(x for x, y in tasks)
        print(tasks, tot)
        start = tot
        
        for x,y in tasks:
            if start < y:
                tot += (y-start)
                start = y - x
            else:
                start -= x
        
        return tot
                