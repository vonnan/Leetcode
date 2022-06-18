class Solution:
    def addBoldTag(self, ss: str, words: List[str]) -> str:
        dic = defaultdict(list)
        if not words:
            return ss
        for word in words:
            dic[word[0]].append(word)
            
        lst = []
        n = len(ss)
        for i,c in enumerate(ss):
            for word in dic[c]:
                m = len(word)
                if ss[i:i+m] == word:
                    lst.append((i, i + m))
        
        lst.sort()
        if not lst:
            return ss
        
        res = []
        
        start, end = lst.pop(0)
        while lst:
            s,e = lst.pop(0)
            if s > end:
                res.append((start, end))
                start, end = s, e
            else:
                end = max(e, end)
            
        res.append((start, end))
        
        ans = ""
        i = 0
        for s,e in res:
            ans += ss[i:s] + "<b>" + ss[s:e] + "</b>"
            i = e
        return ans + ss[i:]
        