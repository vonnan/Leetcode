class Solution:
    def confusingNumberII(self, n: int) -> int:
        dic = {0: 0, 1: 1, 6:9, 8: 8, 9: 6}
        sets = set([0,1,6,8,9])
        
        count = []
        
        def dfs(num, rotation, pos):
            if num != rotation:
                count.append(num)
                
            for digit in sets:
                if num == 0 and digit == 0:
                    continue
                new = num * 10 + digit
                if new <= n:
                    new_ro = dic[digit] * pos  + rotation
                    dfs(new, new_ro, pos * 10)
                    
        dfs(0, 0 , 1)
        
        return len(count)
                    
        