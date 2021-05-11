class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        presum = sum(cardPoints[:k])
        sufsum = 0
        res = presum + sufsum
        for i in range(k-1, -1, -1):
            presum -= cardPoints[i]
            sufsum += cardPoints[-(k-i)]
            res = max(res, presum + sufsum)
        return res
