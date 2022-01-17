class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        size = len(nums)//k
        if len(nums)%k!=0:
            return False
        cnt = [0]*(len(nums)+1)
        for i in nums:
            cnt[i]+=1
        for i in cnt:
            if i>k:
                return -1
        self.res = inf
        res = 0
        memo = {}
        @lru_cache(None)
        def dfs(index,k,currsize,currmin,currmax,cnt):
            if k==0:
                return 0
            res = inf
            for i in range(index,len(nums)+1):
                currnum = i
                
                if cnt[currnum]>0:
                    newcnt = list(cnt)
                    newcnt[currnum]-=1
                    temp1=currmin 
                    temp2= currmax
                    currmin = min(currmin,currnum)
                    currmax = max(currmax,currnum)
                    if currsize+1==size:
                        res= min(res,currmax-currmin+dfs(0,k-1,0,inf,-inf,tuple(newcnt)))
                    else:
                        res = min(res,dfs(i+1,k,currsize+1,currmin,currmax,tuple(newcnt)))
                    
                    currmin = temp1
                    currmax = temp2
            return res
        res = dfs(0,k,0,inf,-inf,tuple(cnt))
        
        return res        
        