class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        sets = set(s)
        dic = {c : (s.index(c), s.rindex(c)) for c in sets}
        
        for char in sets:
            left, right = dic[char]
            right_, left_ = -1, -1
            while right_ != right or left_ != left:
                right_, left_ = right, left
                right = max(dic[c][1] for c in set(s[left: right + 1]))
                left = min(dic[c][0] for c in set(s[left:right + 1]))
            dic[char] = (left, right)
        
        print(dic)
        lst = list(dic.values())
        lst.sort(key = lambda x: (x[0], - x[1]))
        l, r = lst[0]
        res = [r -l +1]
        for left, right in lst[1:]:
            if left < r:
                continue
            else:
                l, r = left, right
                res.append(r - l + 1)
        return res
            
        
        
        