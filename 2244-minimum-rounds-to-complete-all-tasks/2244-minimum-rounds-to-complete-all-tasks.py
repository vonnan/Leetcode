class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = Counter(tasks)
        if min(counter.values()) == 1:
            return -1
        
        res = 0
        for val in counter.values():
            if val == 2 or val == 3:
                res += 1
                continue
                
            q, r = divmod(val, 3)
            res += q
            if r:
                res += 1
        
        return res