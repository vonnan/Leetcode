class Solution:
    def decodeString(self, s: str) -> str:
        stack, num, curr_str = [], "", ""
        
        for c in s:
            if c.isdigit():
                num += c
                
            
            elif c.isalpha():
                curr_str += c
                
            elif c == "[":
                stack.append((num, curr_str))
                num, curr_str = "", ""
            
            elif c == "]":
                pre_num, pre_str = stack.pop()
                curr_str = pre_str + int(pre_num) * curr_str
              
        return curr_str
                
                