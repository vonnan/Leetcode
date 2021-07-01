class Solution:
    def countAndSay(self, n: int) -> str:
        lst =[""] * 31
        lst[0] = "1"
        for i in range(1,n):
            prev, ct  = lst[i-1], 1
            if len(prev) ==1:
                lst[i] = "1" + prev[0]
            
            for j in range(1, len(prev)):
                if prev[j] == prev[j-1]:
                    ct += 1
                    
                else:
                    lst[i] += str(ct) + prev[j-1]
                    ct = 1
                if j == len(prev) -1:
                    lst[i] += str(ct) + prev[j]
        print(lst)    
        return lst[n-1]
        