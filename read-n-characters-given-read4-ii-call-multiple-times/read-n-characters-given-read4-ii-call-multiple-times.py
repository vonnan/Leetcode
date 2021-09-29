# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.q = deque()
    def read(self, buf: List[str], n: int) -> int:
        
        read, remain = 0, n
        
        while remain:
            b = [""]* 4
            read4(b)
            [self.q.append(c) for c in b]
            if not self.q:
                break
                
            while remain and self.q:
                buf[read] = self.q.popleft()
                read += 1
                remain -= 1
                
        return read
                