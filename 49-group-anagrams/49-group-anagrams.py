class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for word in strs:
            counter = Counter(word)
            wd = ""
            for key in sorted(counter):
                wd += key
                wd += str(counter[key])
            dic[wd].append(word)
        return list(dic.values())
        
    