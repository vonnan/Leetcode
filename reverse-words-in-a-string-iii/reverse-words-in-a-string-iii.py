class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split(" ")
        lst = [word[::-1] for word in lst]
        
        return " ".join(lst)