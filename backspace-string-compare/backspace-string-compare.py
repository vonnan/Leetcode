class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backspace(a):
            lst = []
            for c in a:
                if c != "#":
                    lst.append(c)
                else:
                    if lst:
                        lst.pop()
            return "".join(lst)
        
        return backspace(s) == backspace(t)