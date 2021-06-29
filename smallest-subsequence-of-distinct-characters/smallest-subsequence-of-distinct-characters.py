class Solution:
    def smallestSubsequence(self, s: str) -> str:
        seen = set()
        stack, counter = [], Counter(s)
        
        for c in s:
            counter[c] -= 1
            if c not in seen:
                while stack and counter[stack[-1]] and stack[-1] >= c:
                    seen.remove(stack.pop())
                seen.add(c)
                stack.append(c)
        return "".join(stack)
            