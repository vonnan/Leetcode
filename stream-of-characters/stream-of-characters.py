class StreamChecker:

    def __init__(self, words: List[str]):
        self.dic = defaultdict(set)
        self.s = ""
        self.size = 0
        for word in words:
            self.dic[word[-1]].add(word)

    def query(self, letter: str) -> bool:
        self.s += letter
        self.size += 1
        if letter in self.dic:
            for word in self.dic[letter]:
                d = len(word)
                if d > self.size:
                    continue
                else:
                    if word == self.s[-d:]:
                        return True
                
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)