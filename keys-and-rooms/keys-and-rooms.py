class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q, n = deque([0]), len(rooms)
        visited = set([0])
        while q:
            r = q.popleft()
            for key in rooms[r]:
                if key not in visited:
                    visited.add(key)
                    q.append(key)
        return visited == set(range(n))
                    