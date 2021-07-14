class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        left, right = 1, max(bloomDay)
        while left < right:
            mid = (left + right)//2
            ct, res = 0, 0
            for b in bloomDay:
                if b <= mid:
                    ct += 1
                    if ct == k:
                        res += 1
                        ct = 0
                        if res >= m:
                            break
                else:
                    ct = 0
            if res >= m:
                right = mid
            else:
                left = mid + 1
        return left