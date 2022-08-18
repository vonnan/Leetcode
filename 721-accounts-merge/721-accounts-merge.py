class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        UF = {i:i for i in range(n)}
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x,y):
            UF.setdefault(x,x)
            UF.setdefault(y,y)
            UF[find(x)] = find(y)
        
        dic = defaultdict(int)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in dic:
                    union(dic[email], i)
                else:
                    dic[email] = i
        
        
        dic2= defaultdict(set)
        for i in range(n):
            dic2[find(i)] |= set(accounts[i][1:])
        
        res = []
        for key in dic2:
            lst = [accounts[key][0]]
            lst.extend(sorted(list(dic2[key])))
            res.append(lst)
            
        return res
            
        
                