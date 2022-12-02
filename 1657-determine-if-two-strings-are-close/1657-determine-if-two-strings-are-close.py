class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        counter1, counter2 = Counter(word1), Counter(word2)
        val1, val2= sorted(list(counter1.values())), sorted(list(counter2.values()))
        key1, key2 = sorted(list(counter1.keys())), sorted(list(counter2.keys()))
        
        return val1 == val2 and key1== key2