class Solution:
    def numberOfWeakCharacters(self, A: List[List[int]]) -> int:
        res = 0
        curr_max = 0
        A.sort(key = lambda x: (-x[0], x[1]))
        
        for _, d in A:
            if d < curr_max:
                res += 1
            else:
                curr_max = d
        
        return res