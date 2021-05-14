from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        no_go_sets = set(deadends)
        if "0000" in no_go_sets:
            return -1
        if target == "0000":
            return 0
        
        step = 0
        queue = deque(["0000"])
        while queue:
            n = len(queue)
            for _ in range(n):
                combo = queue.popleft()
                if combo == target:
                    return step + 1
                for move in [-1,1]:
                    for i in range(4):
                        new = str((int(combo[i]) + move)%10)
                        new_combo = combo[:i] + new + combo[i+1:]
                        if new_combo == target:
                            return step + 1
                        if new_combo not in no_go_sets:
                            no_go_sets.add(new_combo)
                            queue.append(new_combo)
            step += 1
        return -1