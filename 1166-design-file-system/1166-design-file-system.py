class FileSystem:

    def __init__(self):
        self.dic = defaultdict(int)
        self.dic[""] = 0

    def createPath(self, path: str, value: int) -> bool:
        lst = path.split("/")
        if path in self.dic:
            return False
        elif "/".join(lst[:-1]) in self.dic:
            self.dic[path] = value
            return True
        else:
            return False

    def get(self, path: str) -> int:
        if path in self.dic:
            return self.dic[path]
        return -1


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)