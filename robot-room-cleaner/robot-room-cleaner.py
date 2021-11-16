# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        right = {(0,1): (1, 0), (1,0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1)}
        path = list(right.keys())
        visited = set([])
        
        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
            
        def dfs(r,c, d):
            visited.add((r,c))
            robot.clean()
            for i in range(4):
                nd = (i + d) % 4
                dr, dc = right[path[nd]]
                nr, nc = r + dr, c + dc
                if not (nr, nc)  in visited and robot.move():
                    dfs(nr, nc, nd)
                    go_back()
                
                robot.turnRight()
        
        dfs(0, 0, 0)
        
                
        
        