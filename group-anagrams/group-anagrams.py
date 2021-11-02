class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        res = []
        dic = defaultdict(list)
        for i, s in enumerate(strs):
            x= [0] * 26
            for c in s:
                x[ord(c) - ord("a")] += 1
            dic[tuple(x)].append(s)
        return dic.values()
                
            