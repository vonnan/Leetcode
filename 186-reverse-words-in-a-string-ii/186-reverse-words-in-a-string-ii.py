class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        n = len(s)
        start, end = 0, 0
        for i, c in enumerate(s):
            if c == " ":
                s[start:end] = s[start:end][::-1]
                end += 1
                start = end
            elif i == n-1:
                s[start:] = s[start:][::-1]
            else:
                end += 1
            
            
        
