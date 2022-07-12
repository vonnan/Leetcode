class Solution:
    def maximizeSweetness(self, A: List[int], k: int) -> int:
        k += 1
        left, right = min(A), sum(A)//k
        #print(left, right)
        
        while left < right:
            mid = (left + right)//2
            ct, chunk = 0, 1
            
            for a in A:
                if ct + a <= mid:
                    ct += a
                else:
                    ct = 0
                    chunk += 1
                    if chunk > k:
                        left = mid + 1
                        break
                        
            if chunk <= k:
                right = mid
            
            #print(mid, left, right, ct, chunk)
        
        return left
                
                
                    