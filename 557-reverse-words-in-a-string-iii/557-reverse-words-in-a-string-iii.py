class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        return " ".join([x[::-1] for x in s])