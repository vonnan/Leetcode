class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        row, col = len(board), len(board[0])
        res = set()
        
        for word in words:
            node = trie
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node["$"] = True
        
        def dfs(r,c,node, word):
            ch = board[r][c]
            path = [(0,1), (0, -1), (1, 0), (-1, 0)]
            if ch in node:
                node = node[ch]
                board[r][c] = ""
                if "$" in node:
                    res.add(word + ch)
                for dr, dc in path:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col:
                        dfs(nr, nc, node, word + ch)
                board[r][c] = ch
                
        for r in range(row):
            for c in range(col):
                dfs(r,c,trie, "")
        
        return res
                
                
                