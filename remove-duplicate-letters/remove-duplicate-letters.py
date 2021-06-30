class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if len(s) == 1:
            return s
        seen, stack, counter  = set(), [], Counter(s)
        for c in s:
            counter[c] -= 1
            if c not in seen:
                seen.add(c)
                while stack and stack[-1] > c and counter[stack[-1]]:
                    seen.remove(stack.pop())
                stack.append(c)
        return "".join(stack)
                    
                    
                
                