class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        sets = set()
        for word in dict:
            for i, ch in enumerate(word):
                x = word[:i] + "." + word[i+1:]
                if x in sets:
                    return True
                sets.add(x)
        return False
                