class Solution:
    def boldWords(self, words: List[str], str: str) -> str:
        dic = defaultdict(list)
        interval = []
        for word in words:
            dic[word[0]].append(word)
        
        for i, c in enumerate(str):
            if c in dic:
                for word in dic[c]:
                    n = len(word)
                    if str[i:i+n] == word:
                        interval.append((i, i+n))
        if not interval:
            return str
        
        interval.append((inf, inf))
        
        res = []
        start, end = interval[0]
        for s,e in interval[1:]:
            if s<= end:
                end = max(e, end)
            else:
                res.append((start, end))
                start, end = s, e
        
        
        ans = ""
        start, end = res.pop(0)
        i = 0
        while i < len(str):
            ans += str[i:start] + "<b>" + str[start: end] +"</b>"
            i = end
            if res:
                start, end = res.pop(0)
            else:
                return ans + str[end:]
        return ans
                
                
            
        