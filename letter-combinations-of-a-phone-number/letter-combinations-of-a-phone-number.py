class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"2": "abc", "3":"def", "4": "ghi", "5": "jkl", "6": "mno", "7":"pqrs", "8": "tuv", "9": "wxyz"}
        if not digits:
            return []
        
        digits = deque(list(digits))
        sets= [""]
        
        while digits:
            s = digits.popleft()
            temp = []
            
            for path in sets:
                for c in dic[s]:
                    temp.append(path + c)
                    
            sets = temp[:]
        
        return sets
                