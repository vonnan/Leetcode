class Solution:
    def rearrangeString(self, string: str, k: int) -> str:
        if not string:
            return ''

        count = defaultdict(int)
        for s in string:
            count[s] += 1
        # sort the letters according to the frequency
        stack = sorted(list(count.items()), key=lambda t: t[1])

        char, count = stack.pop()  # get most frequent character
        lst = [[char] for _ in range(count)]
        print(lst, stack)

        # take care of the letters with same highest freq
        while stack and stack[-1][1] == count:
            char, _ = stack.pop()
            for l in lst:
                l.append(char)
        print(lst)

        # all the characters left
        res = ''.join(c*n for c, n in stack)
        print(res)
        # padding
        for i, r in enumerate(res):
            lst[i % (len(lst)-1)].append(r)

        for l in lst[:-1]:
            if len(l) < k:
                return ''

        return ''.join(''.join(l) for l in lst)        
                
                
                
            
        
        
            
        
          