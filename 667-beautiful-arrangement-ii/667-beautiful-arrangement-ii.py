class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        lst = list(range(1, n+1))
        if k == 1:
            return lst
        
        res = [0]* n
        res[:k:2] = lst[-k//2:][::-1]
        res[1:k:2] = lst[:k//2]
        
        if k %2:
            res[k:] = lst[k//2:(-k//2)][::-1]
        else:
            res[k:] = lst[k//2:(-k//2)]
        
        return res
            
        