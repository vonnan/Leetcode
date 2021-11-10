class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        
        def helper(prev_factor, arr, n):
            for i in range(prev_factor, int(n**0.5)+1):
                if n % i ==0:
                    res.append(arr +[i, n//i])
                    helper(i, arr +[i], n//i)
        
        helper(2, [], n)
        
        return res

            