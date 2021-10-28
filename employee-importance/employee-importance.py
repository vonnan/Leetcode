"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        dic = defaultdict(list)
        importance = defaultdict(int)
        
        for e in employees:
            idx, val, sub = e.id, e.importance, e.subordinates
            dic[idx].extend(sub)
            importance[idx] = val
            
        def helper(idx):
            res = importance[idx]
            for sub in dic[idx]:
                res += helper(sub)
            return res
        
        return helper(id)
           
        