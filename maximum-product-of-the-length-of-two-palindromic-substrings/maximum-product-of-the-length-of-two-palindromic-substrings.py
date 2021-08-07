class Solution:
    def maxProduct(self, s: str) -> int:
        if len(s)<4: return 1
        
        # chop off all singles at the start and end
        from collections import Counter
        C = Counter(s)
        while C[s[0]]==1: s=s[1:]
        while C[s[-1]]==1: s=s[:-1]
            
        # if s is all one character or all 2 characters, everything is a palindrome
        #  return max possible way to divide len(s) into two odds
        if s==s[0]*len(s) or s==s[:2]*(len(s)//2):
            q = len(s)//2
            if q&1==0: q-=1
            r = len(s)-q
            if r&1==0: r-=1
            return q*r
			
        # the general case
        maxStartingAtX = [1 for _ in s]
        maxEndingAtX = [1 for _ in s]
        for i in range(len(s)):
            j=1
            while i-j>=0 and i+j<len(s) and s[i-j]==s[i+j]:  # this is theoretically quadratic but in practice linear
			    # note both of these can be done without max's but this is more readable I think
                maxStartingAtX[i-j] = max(maxStartingAtX[i-j],2*j+1)
                maxEndingAtX[i+j] = max(maxEndingAtX[i+j],2*j+1)
                j+=1
			
        # linear time, pretty self explanatory, it's literally the max Starting after the index
        maxStartingAfterX = [0 for _ in s]
        for i in range(len(s)-2,-1,-1):
            maxStartingAfterX[i] = max(maxStartingAfterX[i+1],maxStartingAtX[i+1])

        maxEndingUpToX = 1
        ret = 0
        for i in range(len(s)):
            maxEndingUpToX = max(maxEndingUpToX,maxEndingAtX[i])
            ret = max(ret,maxEndingUpToX * maxStartingAfterX[i])
    
        return ret    
  