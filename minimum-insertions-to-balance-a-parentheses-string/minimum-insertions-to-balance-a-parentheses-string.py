class Solution:
    def minInsertions(self, s: str) -> int:
        res, right = 0, 0
        # res: tot change of brackets so far; right: right brackets that needs to be changed
        for c in s:
            if c=="(":
                right += 2
                res += right %2
                right -= right%2
            if c==")":
                right -= 1
                if right <0:
                    res += 1
                    right += 2
                
        return res + right
                