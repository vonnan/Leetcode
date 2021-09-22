class StreamChecker:

    def __init__(self, words: List[str]):
        self.stack = []
        self.dic = defaultdict(list)
        for word in words:
            self.dic[word[-1]].append(word)
    
    def query(self, letter: str) -> bool:
        self.stack.append(letter)
        if letter not in self.dic:
            return False
        else:
            for word in self.dic[letter]:
                m = len(word)
                if len(self.stack) < m:
                    continue
                else:
                    
                    if "".join(self.stack[-m:]) == word:
                        return True
            return False
            
            
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)