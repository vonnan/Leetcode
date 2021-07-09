class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        left, right, mod = 0, max(inventory), 10 ** 9 + 7
        counts = lambda i: sum(count - i + 1 for count in inventory if count >= i)
        while left < right:
            mid = left + (right - left) // 2
            if counts(mid) > orders:
                left = mid + 1
            else:
                right = mid
        result = sum((count + left) * (count - left + 1) // 2 for count in inventory if count >= left) % mod
        return (result + outbound * (left - 1) if (outbound := orders - counts(left)) > 0 else result) % mod       
           
        
            
            
            
            
        