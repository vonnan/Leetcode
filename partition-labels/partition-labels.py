class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        sets = set(s)
        dic = {c: (s.index(c), s.rindex(c)) for c in sets}
        
        for char in dic:
            left, right = dic[char]
            left_, right_ = -1, -1
            while left_ != left or right_ != right:
                left_, right_ = left, right
                right = max(dic[c][1] for c in set(s[left:right + 1]))
                left = min(dic[c][0] for c in set(s[left: right + 1]))
            dic[char] = (left, right)
            
        lst = list(set(dic.values()))
        lst.sort()
        
        left, right = lst[0]
        res= [right - left + 1]
        for l,r in lst[1:]:
            if l < right:
                continue
            left, right = l, r
            res.append(right - left + 1)
            
        
        return res
            
        