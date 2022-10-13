class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        target = Counter("balloon")
        counter = Counter(text)
        res = 0
        while counter & target == target:
            counter -= target
            res += 1
        return res
            