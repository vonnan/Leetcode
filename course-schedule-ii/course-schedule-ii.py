from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        dic = defaultdict(set)
        
        for course, pre in prerequisites:
            dic[pre].add(course)
            
        tracker = set()
        visited = set()
        stack = []
        
        self.cycle = False
        
        def dfs(node, tracker, visited, stack):
            tracker.add(node)
            visited.add(node)
            
            for course in dic[node]:
                if course in tracker:
                    self.cycle = True
                    break
                    
                if course not in visited:
                    dfs(course, tracker, visited, stack)
                    
            tracker.remove(node)
            stack.append(node)
            
        for course in range(numCourses):
            if course not in visited:
                dfs(course, tracker, visited, stack)
                if self.cycle:
                    return []
                
        return stack[::-1]
                    