class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dic_lose = defaultdict(int)
        set_w = set([])
        
        for a, b in matches:
            dic_lose[b] += 1
            set_w.add(a)
        
        set_l = set([])
        
        for key in dic_lose:
            if key in set_w:
                set_w.remove(key)
            if dic_lose[key] == 1:
                set_l.add(key)
        
        return [sorted(set_w), sorted(set_l)]
            