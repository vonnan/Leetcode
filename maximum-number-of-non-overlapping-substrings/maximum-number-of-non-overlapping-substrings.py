class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        char_set = set(s)
         
        dic = {c: (s.rindex(c), s.index(c)) for c in char_set}
        
        for char in char_set:
            right, left = dic[char]
            right_, left_ = -1, -1
            while right_ != right or left_ != left:
                right_, left_ = right, left
                left = min(dic[c][1] for c in set(s[left: right + 1]))
                right = max(dic[c][0] for c in set(s[left: right + 1]))
            dic[char] = (right, left)
            
        res, curr = [], 0
        
        for right, left in sorted(set(dic.values())):
            if left >= curr:
                res.append(s[left: right + 1])
            curr = right + 1
        return res
            