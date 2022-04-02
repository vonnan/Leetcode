class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie, res = {}, []
        for word in words:
            cur_node = trie
            for letter in word:
                if letter not in cur_node:
                    cur_node[letter] = {}
                cur_node = cur_node[letter]
            cur_node['word'] = word
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, trie, res)
        return res
            
    def dfs(self, board, i, j, cur_node, res):
        if 'word' in cur_node:
            res.append(cur_node['word'])
            cur_node.pop('word')
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] not in cur_node:
            return
        next_node = cur_node[board[i][j]]
        board[i][j] = board[i][j].upper()
        self.dfs(board, i-1, j, next_node, res)
        self.dfs(board, i+1, j, next_node, res)
        self.dfs(board, i, j-1, next_node, res)
        self.dfs(board, i, j+1, next_node, res)
        board[i][j] = board[i][j].lower()
        if not cur_node[board[i][j]]:
            cur_node.pop(board[i][j])