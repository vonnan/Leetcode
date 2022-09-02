from bisect import bisect

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        dic = defaultdict(list)
        def convert(time):
            return int(int(time[:2])* 60 + int(time[-2:]) )
        
        for name, time in zip(keyName, keyTime):
            dic[name].append(convert(time))
            
        for name in dic:
            dic[name].sort()
         
        res = []
        for name in dic:
            lst = dic[name]
            if len(lst) < 3:
                continue
            
            for i, time in enumerate(lst[:-2]):
                if lst[i + 2] <= time + 60:
                    res.append(name)
                    break
        return sorted(res)
                
        
        