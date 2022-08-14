class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        res = []
        edge = collections.defaultdict(set)
        wordList = set(wordList)
        for word in wordList:
            for i in range(len(word)):
                edge[word[:i] +'*'+word[i+1:]].add(word)
        bfsedge = {}

        def bfs():
            minl = 0
            queue = set()
            queue.add(beginWord)
            while queue:
                next_queue = set()
                for word in queue:
                    if word in wordList:
                        wordList.remove(word)
                bfsedge[minl] = collections.defaultdict(set)
                for word in queue:
                    if word == endWord:
                        return minl
                    for i in range(len(word)):
                        for w in edge[word[:i]+'*'+word[i+1:]]:
                            if w in wordList:
                                next_queue.add(w)
                                bfsedge[minl][w].add(word)
                queue = next_queue
                minl += 1
            return minl

        def dfs(seq, endWord):
            if seq[-1] == endWord:
                res.append(seq.copy())
                return
            for nextWord in bfsedge[minl-len(seq)][seq[-1]]:
                if nextWord not in seq:
                    dfs(seq+[nextWord], endWord)

        minl = bfs()
        dfs([endWord], beginWord)
        # reverse the sequence
        for sq in res:
            sq.reverse()
        return res