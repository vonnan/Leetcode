from heapq import heappush
class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        sets = set([0])
        
        for row in mat:
            temp, heap = set(), []
            for num in sorted(row):
                for prev in sorted(sets):
                    if num + prev >= target:
                        heappush(heap, num + prev)
                    else:
                        temp.add(prev + num)
                
                if heap:
                    temp.add(heap[0])
                    
            sets = temp
        
        return min(abs(num -target) for num in sets)
                
                    
        
        
        