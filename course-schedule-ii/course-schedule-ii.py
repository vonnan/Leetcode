class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic = defaultdict(set)
        for course, pre in prerequisites:
            dic[pre].add(course)
        
        visited, tracker, stack = set(), set(), []
        
        self.cycle = False
        
        def dfs(node, visited, tracker, stack):
            visited.add(node)
            tracker.add(node)
            
            for course in dic[node]:
                if course in tracker:
                    self.cycle = True
                    break
                    
                if course not in visited:
                    dfs(course, visited, tracker, stack)
                
            tracker.remove(node)
            stack.append(node)
            
        for course in range(numCourses):
            if course not in visited:
                dfs(course, visited, tracker, stack)
                if self.cycle:
                    return []
        
        return stack[::-1]
                
                
                    
        