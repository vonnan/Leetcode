class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips = sorted(clips, key = lambda x: (x[0], -x[1]))
        start_set = set([x for x,y in clips])
        if T ==0:
            return 0
        if 0 not in start_set:
            return -1
        lst, visited = [], set()
        for s,e in clips:
            if s not in visited:
                lst.append((s,e))
                visited.add(s)
               
        
        end, end2, res = -1, 0, 0
        
        for s,e in lst:
            if end2 >= T or s > end2:
                break
            elif end < s <= end2 and e > end2:
                res, end = res + 1, end2
            end2 = max(end2, e)
        
        return res if end2 >= T else -1
            
        
        
        
            
        
        