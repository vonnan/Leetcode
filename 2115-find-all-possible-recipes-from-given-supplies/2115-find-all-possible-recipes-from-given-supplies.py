class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        res = set([])
        
        supplies = set(supplies)
        tot = supplies | set(recipes)

        q = deque([])
        
        for r,i in zip(recipes, ingredients):
            if set(i) & supplies == set(i):
                res.add(r)
                supplies.add(r)
            else:
                if set(i) & tot == set(i):
                    q.append((r, i))
                
                
        if not q:
            return res
        
        flag = True
        while flag:
            m = len(q)
            for _ in range(m):
                r, i = q.popleft()
                if set(i) & supplies == set(i):
                    res.add(r)
                    supplies.add(r)
                else:
                    q.append((r, i))
            if len(q) == m:
                return res
                
            
            
        
        