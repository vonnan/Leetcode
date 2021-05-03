class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = defaultdict(list)
        
        for course, pre in prerequisites:
            dic[pre].append(course)
            
        def cycle(node, tracker, visited):
            tracker[node] = True
            visited[node] = True
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
            if course not in visited and cycle(course, tracker, visited):
                return False
            
        return True

       
                
            