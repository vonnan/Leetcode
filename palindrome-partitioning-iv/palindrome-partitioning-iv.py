class Solution:
    def checkPartitioning(self, s: str) -> bool:
        counter = Counter(s)
        lst = [ x for x,val in counter.items() if val%2]
        if len(lst) >3:
            return False
        
        def isPalindrom(x):
            return x == x[::-1]
        
        i = 1
        while  i < len(s):
            if not isPalindrom(s[:i]):
                i += 1
                continue
            for j in range(i+1, len(s)):
                x = s[i:j]
                if not isPalindrom(x):
                    continue
                elif isPalindrom(s[j:]):
                    print(s[:i], s[i:j], s[j:])
                    return True
            i += 1
        return False
                    
            
        
        