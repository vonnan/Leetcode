from itertools import permutations
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        arr = map(str, arr)
        lst =[(x[0]+x[1], x[2] + x[3]) for x in permutations(arr)]
        
        lst = sorted([x+":" + y for x,y in lst if int(x) <=23 and int(y) <=59])
        return lst[-1] if lst else ""
        
        
              
        