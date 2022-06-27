
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        dic = {"6":"9", "9": "6"}
        same = {"0", "1", "8"}
        if n == 1:
            return same
        m = n//2
        sets = set(["1", "8", "6", "9"])
        for _ in range( m- 1):
            sets = set([num + c for num in sets for c in "01689"])
        
        def convert(num, n):
            res = ""
            for c in num:
                if c in same:
                    res = c + res
                else:
                    res = dic[c] + res
            return [num + res] if n % 2 ==0 else [num + c + res for c in same]
        
        res = []
        for num in sets:
            res.extend(convert(num, n))
        return res
            
                
        