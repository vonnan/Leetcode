# """
# This is the ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares 4 different elements in the array
#	 # return 4 if the values of the 4 elements are the same (0 or 1).
#	 # return 2 if three elements have a value equal to 0 and one element has value equal to 1 or vice versa.
#	 # return 0 : if two element have a value equal to 0 and two elements have a value equal to 1.
#    def query(self, a: int, b: int, c: int, d: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#

class Solution:
    def guessMajority(self, reader: 'ArrayReader') -> int:
        n = reader.length()
        
        set_3, set_no_3 = set([3]),set([])
        first = reader.query(0,1,2,3)
        if first == 4:
            set_3.add(0)
            set_3.add(1)
            set_3.add(2)
        three = reader.query(0,1,2,4)
        def helper(res, i):
            if res == three:
                set_3.add(i)
            else:
                set_no_3.add(i)
                
        for i in range(4, n):
            if reader.query(0,1,2,i) == first:
                set_3.add(i)
            else:
                set_no_3.add(i)
        
        if len(set_3) > n//2:
            return 3
        
        elif len(set_no_3) > n//2:
            return set_no_3.pop()
        
        else:
            
            zero, one, two = reader.query(1,2,3,4), reader.query(0,2,3,4), reader.query(0,1,3,4)
            helper(zero, 0)
            helper(one, 1)
            helper(two, 2)
            if len(set_3) > n//2:
                return 3
        
            elif len(set_no_3) > n//2:
                return set_no_3.pop()
            
            elif len(set_3) == len(set_no_3):
                return -1
        
        
        
            
        
        
            
        