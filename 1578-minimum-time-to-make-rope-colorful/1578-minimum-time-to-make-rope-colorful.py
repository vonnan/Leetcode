from bisect import insort

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        prev = colors[0]
        cost =  neededTime[0]
        lst = [cost]
        res = 0
        
        for c,t in zip(colors[1:], neededTime[1:]):
            if c != prev:
                res += cost - lst[-1]
                cost = t
                lst = [t]
            else:
                cost += t
                insort(lst, t)
            prev = c
        return res + cost - lst[-1]
                    
                