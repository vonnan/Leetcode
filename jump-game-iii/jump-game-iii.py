class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque([start])
        seen = set([start])
        n = len(arr)
        
        while q:
            node = q.popleft()
            length = arr[node]
            if length == 0:
                return True
            
            left, right = node - length, node  + length
            if 0 <= left < n and left not in seen:
                q.append(left)
                seen.add(left)
            if 0 <= right < n and right not in seen:
                q.append(right)
                seen.add(right)
        
        return False
            