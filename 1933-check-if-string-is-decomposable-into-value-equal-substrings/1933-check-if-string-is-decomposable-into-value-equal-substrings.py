class Solution:
    def isDecomposable(self, s: str) -> bool:
        flag = False
        prev = ""
        ct = 0
        
        for c in s:
            if c != prev:
                if ct % 3==1:
                    return False
                elif ct % 3== 2:
                    if flag:
                        return False
                    else:
                        flag = True
                        ct = 1
                else:
                    ct = 1
            else:
                ct += 1
            prev = c
            #print(c, ct)
        if ct % 3 ==1:
            return False
        elif ct %3 ==2:
            return not flag
        else:
            return flag
            
                    