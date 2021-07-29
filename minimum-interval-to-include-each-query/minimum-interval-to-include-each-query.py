class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(reverse = 1)
        heap = []
        dic = {}
        
        for q in sorted(list(set(queries))):
            while intervals and intervals[-1][0]<= q:
                s,e = intervals.pop()
                if e >= q:
                    heappush(heap, (e-s+1, e))
            while heap and heap[0][1] < q:
                heappop(heap)
            
            dic[q] = heap[0][0] if heap else -1
            
        return [dic[q] for q in queries]
                