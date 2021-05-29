class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dic = defaultdict(list)
        n = len(beginWord)
        
        for word in wordList:
            for i in range(n):
                dic[word[:i] + "*" + word[i+1:]].append(word)
                
        queue = deque([beginWord])
        seen = set()
        step = 1
        
        while queue:
            m = len(queue)
            for _ in range(m):
                q = queue.popleft()
                for i in range(n):
                    mask = q[:i] + "*" + q[i+1:]
                    if mask in dic:
                        for word in dic[mask]:
                            if word == endWord:
                                return step + 1
                            if word not in seen:
                                seen.add(word)
                                queue.append(word)
                        del dic[mask]
            step += 1
        
        return 0