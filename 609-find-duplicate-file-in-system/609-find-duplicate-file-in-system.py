class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        
        for i in range(len(paths)):
            lst = paths[i].split()
            for i in range(1, len(lst)):
                files = (lst[0] + "/"+ lst[i]).split("(")
                dic[files[1][:-1]].append(files[0])
        res = []
        
        for key, val in dic.items():
            if len(val) > 1:
                res.append(val)
        #res.sort(key = len, reverse = 1)
        return res
                