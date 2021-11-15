class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(x):
            ct = 0
            for c in x:
                if c == "(":
                    ct += 1
                elif c == ")":
                    ct -= 1
                    if ct < 0:
                        return False
            return ct == 0
        
        q = deque([s])
        res, visited = set([]), set([])
        
        while q:
            m = len(q)
            flag = False
            for _ in range(m):
                x = q.popleft()
                if isValid(x):
                    flag = True
                    res.add(x)
                else:
                    for i, c in enumerate(x):
                        if c in "()":
                            nxt = x[:i] + x[i+1:]
                            if nxt not in visited:
                                visited.add(nxt)
                                q.append(nxt)
            if flag:
                return res
        else:
            return [""]
                            