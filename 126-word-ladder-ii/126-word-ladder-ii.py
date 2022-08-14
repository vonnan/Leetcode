class Solution:
    def findLadders(self, begin: str, end: str, List: List[str]) -> List[List[str]]:
        dic = defaultdict(set)
        q = deque([begin])
        
        List = set(List + [begin])
        n = len(begin)
        
        #Create a dictionary: for example: dic[*og] = [hog, cog, log], dic[ho*] = [hot, hog]
        for word in List:
            for i in range(n):
                dic[word[:i] + "*" + word[i+1:]].add(word)
        
        # for each level, create an edge dictionary from current word to next word with one character difference
        q = set([begin])
        edges = {}
        level = 0
        while q:
            flag = False
            edges[level] = defaultdict(set)
            m = len(q)
            for word in q:
                List.discard(word)
            nq = set([])
            for word in q:
            
                if word == end:
                    flag = True
                    break
                for i in range(n):
                    nxt = word[:i] + "*" + word[i+1:]
                    for wd in dic[nxt]:
                        if wd in List:
                            edges[level][wd].add(word)
                            nq.add(wd)
                            
            if flag:
                break
            level += 1
            q = nq
        
        res = []
        
        
        def dfs(path):
            last, m = path[0], level  - len(path)
            
            if last == begin:
                res.append(path.copy())
                return
            
            for word in edges[m][last]:
                if word not in path:
                    #print(word)
                    dfs(  [word] + path)
                    
        dfs([end])
        return res
            
                
        