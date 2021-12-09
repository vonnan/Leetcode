class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set([start])
        q = deque([start])
        n = len(arr)
        while q:
            pos = q.popleft()
            val = arr[pos]
            if val == 0:
                return True
            lst = [pos - val, pos + val]
            for x in lst:
                if 0 <= x < n and x not in visited:
                    visited.add(x)
                    q.append(x)
        return False