from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = defaultdict(set)
        for course, pre in prerequisites:
            dic[pre].add(course)
            
        def cycle(node, tracker, visited):
            visited[node] = True
            tracker[node] = True
            for course in dic[node]:
                if course not in visited and cycle(course, tracker, visited):
                    return True
                elif course in tracker:
                    return True
            tracker.pop(node)
            return False
        
        visited = {}
        for course in range(numCourses):
            tracker = {}
            if cycle(course, tracker, visited):
                return False
        return True
            
                
