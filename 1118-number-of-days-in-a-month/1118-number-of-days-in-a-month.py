class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        A, B = set([1,3,5,7,8,10, 12]), set([4,6,9,11])
        if month!= 2:
            if month in A:
                return 31
            else:
                return 30
            
        if year %4 or (year %100 == 0 and year % 400 ):
        
            return 28
        
        return 29
        