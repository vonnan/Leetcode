class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        
        
        left, right = min(sweetness), sum(sweetness)//(k + 1)
        if len(sweetness) == k + 1:
            return left
        
        res  = left
        while left < right:
            mid = (left + right) // 2
            ct = 1
            tot = 0
            for num in sweetness:
                if num + tot <= mid:
                    tot += num
                else:
                    ct += 1
                    tot = 0
                    if ct > k + 1:
                        break
            if ct > k + 1:
                left = mid + 1
            else:
                right = mid
        return left
                    
            