from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dic = defaultdict(set)
        n = len(beginWord)
        
        for wd in wordList:
            for i in range(n):
                dic[wd[:i]+"*"+wd[i+1:]].add(wd)
                
        queue = [beginWord]
        steps = 1
        
        while queue:
            next_q = set()
            
            while queue:
                curr_wd = queue.pop()
                
                if curr_wd == endWord:
                    return steps
                
                for i in range(n):
                    mask = curr_wd[:i] + "*" + curr_wd[i+1:]
                    if endWord in dic[mask]:
                        return steps + 1
                    next_q = next_q.union(dic[mask])
                    del dic[mask]
    
                    next_q -= set(queue)
            
            queue = list(next_q)
            steps += 1
            
        return 0
        
                    
                    
            
        
        
        
        