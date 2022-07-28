class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res, curr = set(), set()
        for a in arr:
            curr = {a | b for b in curr} | {a}
            res |= curr
        
        return len(res)
            
            