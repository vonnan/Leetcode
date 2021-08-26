from heapq import heappush

class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        """
        bits = 1
        
        for row in mat:
            temp = 0
            for num in row:
                temp |= bits << num
            bits = temp
            
        for x in range(5000):
            if bits >> (target + x) & 1 or x < target and bits >> (target - x) & 1:
                return x
                
        """
        
        sets ={0}
        for row in mat:
            temp, heap = set(), []
            for num in row:
                for prev in sorted(sets):
                    if num + prev >= target:
                        heappush(heap, num + prev)
                        break
                    else:
                        temp.add(num + prev)
            if heap:
                temp.add(heap[0])
            sets = temp
        
        return min(abs(x - target) for x in sets)