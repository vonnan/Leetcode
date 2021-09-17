
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        lst = []
        for i, cost in enumerate(costs):
            a, b = cost
            if a > b:
                city = 1
                diff = a - b
            else:
                city = 0
                diff = b - a
                
            lst.append((diff, i, city))
           
        set0, set1, n = set([]), set([]), len(costs)//2
        lst.sort()
        print(lst) 
        while lst and len(set0) < n and len(set1) < n:
            _, i, city = lst.pop()
            if city== 0:
                set0.add(i)
            else:
                set1.add(i)
        res = 0
        print(set0, set1)
        if len(set0)==n:
            for i, cost in enumerate(costs):
                if i in set0:
                    res += cost[0]
                else:
                    res += cost[1]
            return res
        else:
            for i, cost in enumerate(costs):
                if i in set1:
                    res += cost[1]
                else:
                    res += cost[0]
            return res
        
                
            
                
                