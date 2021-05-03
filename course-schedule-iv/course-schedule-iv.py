from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        matrix = [[False]*numCourses for _ in range(numCourses)]
        
        for course, pre in prerequisites:
            matrix[pre][course] = True
            
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    matrix[i][j] |= matrix[i][k] and matrix[k][j]
        
        res = []
        
        for course, pre in queries:
            res.append(matrix[pre][course])
            
        return res