class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dp = [[False]* numCourses for _ in range(numCourses)]
        
        for course, pre in prerequisites:
            dp[pre][course] = True
            
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    dp[i][j] |= dp[i][k] and dp[k][j]
        
        res = []
        
        for course, pre in queries:
            res.append(dp[pre][course])
            
        return res