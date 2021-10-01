
class AutocompleteSystem:

    def __init__(self, A: List[str], times: List[int]):
        self.prefix = defaultdict(defaultdict)
        self.counter = Counter()
        
        for i, a in enumerate(A):
            n = len(a)
            pre = a[0]
            self.counter[a] = times[i]
            self.prefix[pre][a] = times[i]
            for c in a[1:]:
                pre += c
                self.prefix[pre][a] = times[i]
        self.char = ""
        
    
    def input(self, c: str) -> List[str]:
        if c == "#":
            self.counter[self.char] += 1
            pre = self.char[0]
            self.prefix[pre][self.char] = self.counter[self.char]
            for c in self.char[1:]:
                pre += c
                self.prefix[pre][self.char] = self.counter[self.char]                      
            self.char = ""
            return []
        
        self.char += c
        if self.char in self.prefix:
            lst =sorted([(pre, val) for pre, val in self.prefix[self.char].items()], key = lambda x: (-x[1], x[0]))
            return [pre for pre, _ in lst][:3]

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)