class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = Counter(words)
        lst = [val for word, val in counter.items() if word[0] == word[1]]
        res = sum(val//2 for val in lst) * 4 + 2 * any(val % 2 for val in lst)
        
        
        sets = set([])
        print(res, lst)
        for key in counter:
            if key not in sets and key[0] != key[1] and (key[::-1] in counter):
                res += 4*(min(counter[key], counter[key[::-1]]))
        
                sets.add(key)
                sets.add(key[::-1])
            
        
        return res
        
                    
        