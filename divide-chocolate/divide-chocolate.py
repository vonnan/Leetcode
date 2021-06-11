class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        left, right = min(sweetness), sum(sweetness)//(K+1)
        res = right
        while left < right:
            mid = (left + right)//2
            ct, group = 0, 1
            for x in sweetness:
                if ct + x > mid:
                    group += 1
                    ct = 0
                    if group > K + 1:
                        break
                else:
                    ct += x
            if group > K + 1:
                left = mid + 1
            else:
                right = mid
        
        return left
            
                