class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name, typed = list(name), list(typed)
        while name:
            first = name.pop(0)
            if not typed or typed[0] != first:
                return False
            else:
                typed.pop(0)
            
            if not typed and not name:
                return True
            
            if typed and name and typed[0] != name[0]:
                while typed and typed[0] == first:
                    typed.pop(0)
            
        while typed and typed[0] == first:
            typed.pop(0)
            
        return not typed
            
                
       