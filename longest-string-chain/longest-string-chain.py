class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = len)
        dic = defaultdict(int)
        for word in words:
            n = len(word)
            for i in range(n):
                nxt = word[:i] + word[i+1:]
                dic[word] = max(dic[word], dic[nxt] + 1)
        return max(dic.values())