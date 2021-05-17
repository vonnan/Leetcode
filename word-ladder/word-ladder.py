from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        dic, n = defaultdict(list), len(beginWord)
        for word in wordList:
            for i in range(n):
                dic[word[:i]+"*"+word[i+1:]].append(word)
        
        queue = deque([beginWord])
        visited = set()
        step = 1
        
        while queue:
            m = len(queue)
            for _ in range(m):
                q = queue.popleft()
                if q == endWord:
                    return step + 1
                for i in range(n):
                    mask = q[:i] + "*" + q[i+1:]
                    if mask in dic:
                        for word in dic[mask]:
                            if word == endWord:
                                return step + 1
                            if word not in visited:
                                visited.add(word)
                                queue.append(word)
                        del dic[mask]
            step += 1
        return 0
                