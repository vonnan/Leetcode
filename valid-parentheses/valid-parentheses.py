class Solution:
    def isValid(self, s: str) -> bool:
        while ("{}" in s) | ("[]" in s) | ("()" in s):
            s = s.replace("[]", "").replace("{}", "").replace("()","")
        return s== ""