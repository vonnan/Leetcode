class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        sets = set(deadends)
        queue = deque(["0000"])
        
        if "0000" in sets:
            return -1
        
        sets.add("0000")
        steps = 0
        
        while queue:
            length = len(queue)
            
            for _ in range(length):
                combo = queue.popleft()
                if combo == target:
                    return steps
                
                for i in range(4):
                    for move in [-1, 1]:
                        new_move = (int(combo[i]) + move) % 10
                        new_combo = combo[:i] + str(new_move) +combo[i+1:]
                        if new_combo == target:
                            return steps + 1
                        if new_combo not in sets:
                            sets.add(new_combo)
                            queue.append(new_combo)
            steps += 1            
        return -1
                    
                        
            