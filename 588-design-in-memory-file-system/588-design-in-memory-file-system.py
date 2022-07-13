class Node(object):
    def __init__(self):
        self.children = {}
        
    def setdefault(self, token):
        return self.children.setdefault(token, Node())
        
    def get(self, token):
        return self.children.get(token, None)
                          
class FileSystem(object):
    def __init__(self):
        self.root = Node()
        self.fileinfo = collections.defaultdict(str)
        
    def ls(self, path):
        if path in self.fileinfo:
            return path.split('/')[-1:]

        cur = self.root
        for token in path.split('/'):
            if cur and token:
                cur = cur.get(token)

        return sorted(cur.children.keys()) if cur else []

    def mkdir(self, path):
        cur = self.root
        for token in path.split('/'):
            if token: cur = cur.setdefault(token)
                
    def addContentToFile(self, filePath, content):
        self.mkdir(filePath)
        self.fileinfo[filePath] += content

    def readContentFromFile(self, filePath):
        return self.fileinfo[filePath]
    
# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)