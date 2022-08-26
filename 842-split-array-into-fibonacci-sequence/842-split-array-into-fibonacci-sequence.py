class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        self.res = []
        n = len(num)
        
        def dfs(pos, path):
            if path:
                if len(path[-1]) > 1 and path[-1][0] == "0":
                    return
                
                if int(path[-1]) > 2** 31:
                    return
                
                if len(path) > 2:
                    if int(path[-3]) + int(path[-2]) != int(path[-1]):
                        return
                
                    if pos == n:
                        self.res = path[:]
                        print(path)
                        return
                
            for nxt in range(pos + 1, n + 1):
                dfs(nxt, path + [num[pos : nxt]])
        
        dfs(0, [])
        return [int(c) for c in self.res] if self.res else []
                
                
