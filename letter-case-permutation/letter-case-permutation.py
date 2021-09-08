class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = [""]
        
        for ch in s:
            if ch.isdigit():
                for i in range(len(res)):
                    res[i] += ch
            else:
                for i in range(len(res)):
                    temp = res[i]
                    res[i] += ch.lower()
                    res.append(temp + ch.upper())
        return res
                    