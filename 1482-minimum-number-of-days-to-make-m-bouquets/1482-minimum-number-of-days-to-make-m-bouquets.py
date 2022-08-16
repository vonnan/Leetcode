class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        
        left, right = min(bloomDay), max(bloomDay)
        
        while left < right:
            mid = (left + right)//2
            tot, ct = 0, 0
            for b in bloomDay:
                if b <= mid:
                    ct += 1
                    if ct == k:
                        tot += 1
                        if tot ==m:
                            break
                        ct = 0
                else:
                    ct = 0
            
            if tot >= m:
                right = mid
            else:
                left = mid + 1
        return left