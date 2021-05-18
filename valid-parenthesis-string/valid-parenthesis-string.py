class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        At any point, # of right brackets can not exceed the number of left brackets
        
        the upper limit for the # left brackets is the number of "(" + number of "*" so far, substracted by number of right bracket...this value can not be 
        
        the lower limit for the # left brackets is the number of "(" 
        """
        while "()" in s:
            s = s.replace("()", "")
            
        upper, lower = 0, 0
        
        for char in s:
            if char == "(":
                lower += 1
            else:
                #else means that char == ")" or char =="*"
                lower -= 1
            if char != ")":
                #means that char == "(" or char =="*"
                upper += 1 
            else:
                upper -= 1
                if upper < 0:
                    break
            lower = max(lower, 0)
            
        return lower == 0