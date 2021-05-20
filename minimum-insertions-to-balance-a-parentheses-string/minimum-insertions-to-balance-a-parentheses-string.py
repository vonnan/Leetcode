class Solution:
    def minInsertions(self, s: str) -> int:
        res, right_goal = 0, 0
        for c in s:
            if c == "(":
                right_goal += 2
                res += right_goal%2
                right_goal -= right_goal%2
            
            if c == ")":
                right_goal -= 1
                if right_goal < 0:
                    res += 1
                    right_goal += 2
        
        return res + right_goal