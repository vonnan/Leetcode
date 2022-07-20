class Solution:
    def decodeString(self, s: str) -> str:
        stack, word, num = [], "", ""
        
        for c in s:
            if c.isalpha():
                word += c
            elif c.isdigit():
                num += c
            elif c == "[":
                stack.append((word, num))
                word, num = "", ""
            else:
                prestr, prenum = stack.pop()
                word = prestr +  int(prenum) * word 
        return word