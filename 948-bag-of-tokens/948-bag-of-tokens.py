class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        
        while tokens:
            if tokens[0] <= power:
                score += 1
                power -= tokens.pop(0)
            else:
                if len(tokens) == 1:
                    return score
                if score >= 1:
                    power += tokens.pop()
                    score -= 1
                else:
                    return score
            
        return score
                