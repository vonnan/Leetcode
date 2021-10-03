class Solution:
    def minWindow(self,S: str, T: str) -> str:
        chpositions = collections.defaultdict(deque)
        start = count = -1
        
        for i, ch in enumerate(T):
            chpositions[ch].appendleft(i)  # we'll be iterating from last to first
            
        startpositions = [-1] * len(T)
        for i, ch in enumerate(S):
            if ch not in chpositions: continue
            for pos in chpositions[ch]:
                if pos == 0: startpositions[0] = i
                else: startpositions[pos] = startpositions[pos-1]
                if pos == len(T) - 1 and (start == -1 or count > i - startpositions[-1] + 1):
                    start = startpositions[-1]
                    count = i - startpositions[-1] + 1
        if start < 0: return ''
        return S[start:start+count]