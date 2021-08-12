class Solution:
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n==1:
            return 9
        high=10**n
        low=10**(n-1)
        top = ((high-1)//11)*11
        
        for i in range(high-1,low-1,-1):
            w=int(str(i)+str(i)[::-1])
            for j in range(top,i+1, -11):
                if w%j==0:
                    z=w//j
                    if z<high and z>=low:
                        return w%1337
        """            
        if n == 1: return 9
        for z in range(2, 2 * (9 * 10**n) - 1):
            left = 10**n - z
            right = int(str(left)[::-1])
            root_1, root_2 = 0, 0
						
            if z**2 - 4*right < 0:
                continue
            else:
                root_1 = 1/2 * (z + (z**2-4*right)**0.5)
                root_2 = 1/2 * (z - (z**2-4*right)**0.5)
                if root_1.is_integer() or root_2.is_integer():
                    print(root_1, root_2,10**n*left+right, z)
                    return (10**n*left+right)%1337
             """        