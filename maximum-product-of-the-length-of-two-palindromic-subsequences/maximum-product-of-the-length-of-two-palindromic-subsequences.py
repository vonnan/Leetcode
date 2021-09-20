class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        lst = []
        for mask in range(1, 1<<n):
            subsq = ""
            for i in range(n):
                if mask & (1 <<i):
                    subsq += s[i]
            if subsq == subsq[::-1]:
                lst.append((len(subsq), mask))
       
        lst.sort(reverse= 1)
        print(lst)
        res = 1
        for i in range(len(lst)):
            l1, mask1 = lst[i]
            
            for j in range(i + 1, len(lst) ):
                l2, mask2 = lst[j]
                if mask1 & mask2==0 and l1 * l2 > res:
                    res = l1 * l2
                    break
        
        return res
            
                    
        
        
            
        
            