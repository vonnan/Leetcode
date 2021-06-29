
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        seen, stack = set(), []
        
        for c in s:
            counter[c] -= 1
            while c not in seen and stack and counter[stack[-1]] and stack[-1] >= c:
                seen.remove(stack.pop())
            if c not in seen:
                seen.add(c)
                stack.append(c)
        
        return "".join(stack)