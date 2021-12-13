class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        
        def helper(prev, arr, m):
            for i in range(prev, int(m**0.5) +1):
                if m % i == 0:
                    res.append(arr + [i, m//i])
                    helper(i, arr + [i], m//i)
        
        helper(2, [], n)
        return res