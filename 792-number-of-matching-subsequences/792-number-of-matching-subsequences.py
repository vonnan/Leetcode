class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        res, n = 0, len(s)
        for word in words:
            l_w = len(word)
            if l_w > n:
                continue
            idx = 0
            flag = True
            for i, ch in enumerate(word):    
                if ch not in s[idx:]:
                    flag = False
                    break
                idx = s.find(ch, idx)
                if n-1-idx < l_w - 1-i:
                    flag = False
                    break
                idx += 1
            if flag:
                res += 1
        return res
                    
                
                        
                    
            