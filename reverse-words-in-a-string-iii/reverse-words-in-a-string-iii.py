class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        s = " ".join([x[::-1] for x in s])
        return s