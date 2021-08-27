class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        need = 1
        for val in preorder.split(','):
            if not need:
                return False
            need -= ' #'.find(val)
        return not need
