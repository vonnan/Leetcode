
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        """
    The find() method finds the first occurrence of the specified value.

    The find() method returns -1 if the value is not found.

    The find() method is almost the same as the index() method, the only difference         is that the index() method raises an exception if the value is not found. (See          example below)

    Syntax
    string.find(value, start, end)

        """
        
        start, count = 0, 0
        
        for char in target:
            start = source.find(char, start)
            
            if start ==-1:
                start = source.find(char)
                count += 1
                
                if start ==-1:
                    return -1
                
            start += 1
            
        return count + 1
            

            