class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        
        char_set = set(s)
        n, m = len(s), len(char_set)
         
        dic = {c: (s.rindex(c), s.index(c)) for c in char_set}
        
        for char in dic:
            right, left = dic[char]
            right_, left_ = -1, -1
            while right_ != right or left_ != left:
                right_, left_ = right, left
                left = min(dic[c][1] for c in set(s[left: right + 1]))
                right = max(dic[c][0] for c in set(s[left: right + 1]))
            dic[char] =(right, left)
        
        curr = 0
        res = []
        
        for r, l in sorted(dic.values()):
            
            if l >=curr:
                res.append(s[l:r+1])
            curr = r
           
        
        return res
                
                
            
                
            
            
            
        
            
            