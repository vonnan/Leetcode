class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q, n = deque([0]), len(rooms)
        
        visited = set([0])
        
        while q:
            lst = rooms[q.popleft()]
            for room in lst:
                if room not in visited:
                    visited.add(room)
                    q.append(room)
                    if len(visited) == n:
                        return True
        return False