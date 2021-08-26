from heapq import heappush

class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        """
        sets = {0}
        
        for row in mat:
            temp, heap = set(), []
            for num in row:
                for prev in sorted(list(sets)):
                    if num + prev > target:
                        heappush(heap, num + prev)
                        break
                    else:
                        temp.add(num + prev)
            if heap:
                temp.add(heap[0])
            
            sets = temp
        return min(abs(target - num) for num in sets)
        """       
        nums = {0}
        
        for row in mat:
            nums = {num + prev for prev in nums for num in row }
            
        return min(abs(n - target) for n in nums)
        