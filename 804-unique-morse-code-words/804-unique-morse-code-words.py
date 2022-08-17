class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        lst = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = set([])
        for word in words:
            code = ""
            for c in word:
                code += lst[ord(c) - ord("a")]
            res.add(code)
        return len(res)