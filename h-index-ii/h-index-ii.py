class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        
        if citations[-1] <1:
            return 0
        
        for i, cite in enumerate(citations):
            if cite >= n-i:
                return n -i
        