class Solution:
    def maxRunTime(self, n: int, b: List[int]) -> int:
        b.sort()
        tot = sum(b)
        avg = tot//n
        
        while b and b[-1] > avg:
            tot -= b.pop()
            n-=1
            if n == 0:
                return avg
            avg = tot//n
        return avg
       