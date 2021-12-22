class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key = len)
        res = []
        sets = set(words)
        for word in words[::-1]:
            n = len(word)
            if n == 1:
                if not res or len(res[-1]) ==1:
                    res.append(word)
                    continue
            pre = ""
            flag = True 
            for i in range(n):
                pre += word[i]
                if pre not in sets:
                    flag = False
                    break
            if flag:
                if (not res or len(res[-1])== n):
                    res.append(word)
                else:
                    res.sort()
                    return res[0]
        if not res:
            return ""
        res.sort()
        return res[0] 