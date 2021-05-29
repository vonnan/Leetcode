class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right)//2
            days, curr = 1, 0
            for w in weights:
                if curr + w > mid:
                    days += 1
                    curr = w
                else:
                    curr += w
            if days > D:
                left = mid + 1
            else:
                right = mid
        return left
                    