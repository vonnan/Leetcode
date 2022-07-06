class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        n = len(word)
        words = [word, word[::-1]]
        row, col = len(board), len(board[0])
        for B in board, zip(*board):
            for row in B:
                lst = "".join(row).split("#")
                for s in lst:
                    for word in words:
                        if len(s) == n:
                            if all(s[i] == word[i] or s[i]== " " for i in range(n)):
                                return True
        return False
        
        