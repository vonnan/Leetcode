from bisect import insort
class Solution:
    def minTransfers(self, trans: List[List[int]]) -> int:
        def dfs(i,st):#allocate from pos[i]
            if i==len(pos):
                return 0
            if pos[i]==0:
                return dfs(i+1,0)
            res=len(pos)*len(neg)
            for j in range(st,len(neg)):
                if neg[j]!=0:
                    give=-neg[j] if pos[i]+neg[j]>=0 else pos[i]
                    neg[j]+=give
                    pos[i]-=give
                    res=min(res,1+dfs(i,j+1))
                    neg[j]-=give
                    pos[i]+=give
            return res
        
        balance=collections.Counter()
        for x,y,val in trans:
            balance[x]-=val
            balance[y]+=val
        pos,neg=[],[]
        for _,bal in balance.items():
            if bal>0:
                pos.append(bal)
            elif bal<0:
                neg.append(bal)
        return dfs(0,0)   