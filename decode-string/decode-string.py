class Solution:
    def decodeString(self, s: str) -> str:
        stack, num, strs = [], "", ""
        for c in s:
            if c.isdigit():
                num += c
            elif c.isalpha():
                strs += c
            elif c == "[":
                stack.append((num, strs))
                num, strs = "", ""
            else:
                pre_num, pre_str = stack.pop()
                strs = pre_str + int(pre_num) * strs
        return strs