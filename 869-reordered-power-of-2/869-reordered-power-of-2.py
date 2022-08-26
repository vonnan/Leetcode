class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        if n == 1:
            return True
        
        lst = [pow(2, i) for i in range(32)]
        if n in lst:
            return True
        
        counter = Counter(str(n))
        n = str(n)
        m = len(n)
        res = sorted([(key, val) for key, val in counter.items()])
        
        for num in lst:
            num = str(num)
            if len(num) > m:
                return False
            if len(num) < m:
                continue
                
            if sorted([(key, val) for key, val in Counter(str(num)).items()]) == res:
                return True
        
        return False
        
        
        
    
        
        