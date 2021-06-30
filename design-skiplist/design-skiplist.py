class Skiplist:

    def __init__(self):
        self.d = {}

    def search(self, target):
        """
        :type target: int
        :rtype: bool
        """
        if target in self.d and self.d[target] > 0:
            return True
        return False

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num not in self.d:
            self.d[num] = 1
        else:
            self.d[num] += 1
        

    def erase(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        if num in self.d and self.d[num] != 0:
            self.d[num] -= 1
            return True
        
        return False
        

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)