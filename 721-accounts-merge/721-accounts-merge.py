class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        UF = {}
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]
        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)
        
        cluster = defaultdict(set)
        email_2_name = {}
        for account in accounts:
            name = account[0]
            emails = account[1:]
            for email in emails:
                email_2_name[email] = name
                union(email, emails[0])
         
        for email in UF:
            cluster[find(email)].add(email)
        
        return [[email_2_name[key]] + sorted(list(val)) for key, val in cluster.items()]
        
        
        
                