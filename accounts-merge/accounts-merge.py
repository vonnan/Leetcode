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
            
        cluster = defaultdict(list)
        email_to_name = {}
        
        for account in accounts:
            name = account[0]
            emails = account[1:]
            for email in emails:
                email_to_name[email] = name
                union(emails[0], email)
                
        for email in email_to_name:
            cluster[find(email)].append(email)
            
        return [[email_to_name[key]] + sorted(cluster[key]) for key in cluster]
                
        
            
            
        