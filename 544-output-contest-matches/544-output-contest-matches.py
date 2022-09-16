class Solution:
    def findContestMatch(self, n: int) -> str:
        group = list(map(str, range(1, n + 1)))
        
        while len(group) > 1:
            new = []
            while len(group) >= 2:
                new.append(("(" + group.pop(0) + "," + group.pop() + ")"))
            group = new
            
        return group[0]
        
        
            