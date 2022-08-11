class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        tot = sum(chalk)
        k %= tot
        if k == 0:
            return 0
        
        
        for i, num in enumerate(chalk):
            k -= num
            if k < 0:
                return i