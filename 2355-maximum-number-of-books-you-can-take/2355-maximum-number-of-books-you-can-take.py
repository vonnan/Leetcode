class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        stack = []
        res = books[0]
        for i, book in enumerate(books):
            while stack and  books[stack[-1][0]] >= book - (i - stack[-1][0]):
                stack.pop()
            
            prev_idx, prev_val = -1, 0
            if stack:
                prev_idx, prev_val = stack[-1]
            h = min((i - prev_idx), book)
            ct = prev_val + h * (book + book - h + 1)//2
            res = max(res, ct)
            stack.append((i, ct))
        
        return res
            
        
        
            
                    
                    
            