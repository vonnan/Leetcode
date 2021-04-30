class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        sets = set(deadends+["0000"])
        queue = deque(["0000"])
        if target =="0000":
            return 0
        
        if "0000" in deadends or target in deadends:
            return -1
        
        steps = 0
        
        while queue:
            length = len(queue)
            steps += 1
            for _ in range(length):
                combo = queue.popleft()
                for i in range(4):
                    for move in [-1, 1]:
                        new_move = (int(combo[i]) + move) % 10
                        new_combo = combo[:i] + str(new_move) +combo[i+1:]
                        if new_combo == target:
                            return steps
                        if new_combo not in sets and new_combo not in queue:
                            sets.add(new_combo)
                            queue.append(new_combo)
                            
        return -1
                    
                        
            