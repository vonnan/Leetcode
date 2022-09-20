class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        
        for path in paths:
            path = path.split()
            for i in range(1, len(path)):
                path[i] = path[i].split("(")
                directory = path[0] + "/" + path[i][0]
                file = path[i][1][:-1]
                dic[file].append(directory)
        
        return [x for x in dic.values() if len(x) > 1]