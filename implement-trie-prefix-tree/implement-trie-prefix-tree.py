class Trie:

    def __init__(self):
        self.w = set([])
        self.pre = set([])

    def insert(self, word: str) -> None:
        self.w.add(word)
        n = len(word)
        p = ""
        for i in range(n):
            p += word[i]
            self.pre.add(p)

    def search(self, word: str) -> bool:
        return word in self.w

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.pre


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)