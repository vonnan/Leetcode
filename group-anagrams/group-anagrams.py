class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            x = "".join(sorted(s)) 
            if x in dic:
                dic[x].append(s)
            else:
                dic[x] = [s]
        return [ val for val in dic.values()]

                
        
        