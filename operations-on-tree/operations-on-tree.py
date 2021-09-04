class LockingTree:

    def __init__(self, parent: List[int]):
        self.p = {}
        self.children = defaultdict(list)
        for i, num in enumerate(parent):
            self.p[i] = num
            self.children[num].append(i)
            
        self.lk = {}
        self.unlk = set([i for i in range(len(parent))])
        

    def lock(self, num: int, user: int) -> bool:
        if num not in self.lk:
            self.lk[num] = user
            self.unlk.remove(num)
            return True
        else:
            return False
            

    def unlock(self, num: int, user: int) -> bool:
        if num in self.lk and self.lk[num] == user:
            self.unlk.add(num)
            del self.lk[num]
            return True
        else:
            return False
        

    def upgrade(self, num: int, user: int) -> bool:
        if num in self.lk:
            return False
        
        temp = num
        while temp:
            temp = self.p[temp]
            if temp in self.lk:
                return False
        
        
        q = deque(self.children[num])
        flag = False
        while q:
            m = len(q)
            for _ in range(m):
                x = q.popleft()
                if x in self.lk:
                    flag = True
                    del self.lk[x]
                    self.unlk.add(x)
                if x in self.children:
                    q.extend(self.children[x])
        if flag:
            self.lk[num] = user
            return True
        else:
            return False
                
            
        
            
            
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)