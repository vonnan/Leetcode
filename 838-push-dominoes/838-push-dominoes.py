class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        stack =[]
        res = ""
        prev = ""
        
        for c in dominoes:
            m = len(stack)
            if c == "R":
                if prev !="R":
                    res += "."* m + c
                else:
                    res += "R" * (m + 1)
                prev = c
                stack = []
            elif c == "L":
                if prev != "R":
                    res += "L" * (m + 1)
                else:
                    temp = "R" * (m//2)
                    if m %2:
                        temp += "."
                    temp += "L"*(m//2)
                    res += temp + c
                prev = c 
                stack = []
            elif c == ".":
                stack.append(c)
            
        
        if stack:
            if prev!= "R":
                res += "."* len(stack)
            else:
                res += "R"* len(stack)
        
        return res
            
            
        

           
                
