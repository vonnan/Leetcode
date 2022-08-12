from bisect import bisect_left

class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        s = [max(str, str[::-1]) for str in strs]
        dic = defaultdict(set)
        for i, word in enumerate(s):
            for c in word:
                dic[c].add(i)
        
        max_ = max(dic.keys())
        candidate = dic[max_]
        
        ans = "".join(s)
        for i, word in enumerate(s):
            if i not in candidate:
                continue
            else:
                for j, c in enumerate(word):
                    if c == max_:
                        ans = max(ans, word[j:] + "".join(s[i+1:]) + "".join(s[:i]) + word[:j])
                word = word[::-1]
                for j, c in enumerate(word):
                    if c == max_:
                        ans = max(ans, word[j:] + "".join(s[i+1:]) + "".join(s[:i]) + word[:j])
        return ans

        
        
        