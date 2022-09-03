class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        dic = defaultdict(set)
        
        for i in range(10):
            if i + k < 10:
                dic[str(i)].add(str(i+k))
            if i - k >= 0:
                dic[str(i)].add(str(i-k))
        
        sets = set([str(i) for i in range(1, 10) if dic[str(i)]])
        
        for _ in range(n - 1):
            new = set([])
            for word in sets:
                last = word[-1]
                new |=set([word + c for c in dic[last]])
            sets = new
        return sets
                
        
                
        