class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        operator = ["+", "-", "*", ""]
        
        lst = [num[0]]
        
        for n in num[1:]:
            temp = []
            
            for x in lst:
                for o in operator:
                    temp.append(x + o + n)
            
            lst = temp[:]
        
        res = []
        for x in lst:
            temp = x.replace("*", "+").replace("-", "+")
            flag = False
            for s in temp.split("+"):
                if len(s) >1 and s[0] =="0":
                    flag = True
                    break
            if not flag:
                res.append(x)
                
        return [x for x in res if eval(x) == target]
                