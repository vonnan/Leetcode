from bisect import bisect

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        n = max(persons) + 1
        ct = [0] * n
        self.lst = [[times[0], persons[0]]]
        ct[persons[0]] = 1
        prev = persons[0]
        max_ = 1
        for p, t in zip(persons[1:], times[1:]):
            ct[p] += 1
            if ct[p] >= max_:
                self.lst.append([t, p])
                prev = p
                max_= ct[p]
            else:
                self.lst.append([t, prev])
            
            

    def q(self, t: int) -> int:
        idx = bisect(self.lst, [t, inf])- 1
        return self.lst[idx][1]
        
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)