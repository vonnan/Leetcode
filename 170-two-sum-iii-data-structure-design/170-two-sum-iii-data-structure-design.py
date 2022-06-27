
class TwoSum:

    def __init__(self):
        self.counter = Counter()
        
    def add(self, number: int) -> None:
        self.counter[number] += 1
        
    def find(self, value: int) -> bool:
        for key, val in self.counter.items():
            if key * 2 == value:
                if val > 1:
                    return True
            elif value - key in self.counter:
                return True
        return False
        
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)