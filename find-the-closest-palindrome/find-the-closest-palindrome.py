class Solution:
    def nearestPalindromic(self, n: str) -> str:
        m = len(n)
        if m == 1:
            return str(int(n)-1)
        if int(n) -1 == int("9"* (m-1)) or int(n)-2 == int("9"*(m-1)):
            return "9"*(m-1)
        
        lst = list(n)
        if n==n[::-1]:
            if set(n) == {"9"}:
                    return str(int(n) + 2)
            if not m%2:
                
                if lst[m//2] == lst[m//2 - 1] == "9" and len(set(lst)) != 1:
                    x = str(int(n[:m//2])+1)
                else:
                    x = str(int(n[:m//2])-1)
                res = x + x[::-1]
                return res
            else:
                x = str(int(n[:m//2])+1)
                y = str(int(n[:m//2])-1)
                candidates= []
                if int(n[m//2]) >0:
                    md = str(int(n[m//2]) - 1)
                    candidates.append(n[:m//2] + md + n[:m//2][::-1])
                if int(n[m//2]) == 0:
                    md = "1"
                    candidates.append(n[:m//2] + "1" + n[:m//2][::-1])
                    candidates.append(y + "9" + y[::-1])
                diff, prev, res = int(n), int(n*2), n
                for c in candidates:
                    if abs(int(c)-int(n))<= diff:
                        diff = abs(int(c)-int(n))
                        if int(c) < prev or abs(int(c)-int(n))< diff:
                            res = c
                            prev = int(c)
                return res          
        
        else:
            if not m%2:
                x = [str(int(n[:m//2])), str(int(n[:m//2]) + 1), str(int(n[:m//2]) -1)]
                candidates = [y + y[::-1] for y in x]
                diff, prev, res = int(n), int(n*2), n
                print(candidates)
                for c in candidates:
                    
                    if abs(int(c)-int(n))<= diff:
                        
                        if abs(int(c)-int(n))< diff:
                            res = c
                            prev = int(c)
                        elif int(c) < prev:
                            res = c
                            prev = int(c)
                        diff = abs(int(c)-int(n))
                    print(c, n, abs(int(c)-int(n)), diff, res)
                return res     
                
            else:
                x = str(int(n[:m//2]))
                diff = abs(int(x + n[m//2] + x[::-1]) - int(n))
                front = [str(int(n[:m//2])), str(int(n[:m//2])-1)]
                mid = [n[m//2]]
                if int(n[m//2]) >0:
                    mid.append(str(int(n[m//2]) -1))
                if int(n[m//2]) <9:
                    mid.append(str(int(n[m//2]) + 1))
                res = prev = x + n[m//2] + x[::-1]
                for x in front:
                    for md in mid:
                        candidate = x + md + x[::-1]
                        if abs(int(candidate) - int(n)) <= diff:
                            if abs(int(candidate) - int(n)) < diff or (abs(int(candidate) - int(n)) == diff and candidate < prev):
                                res = candidate
                            diff = abs(int(candidate) - int(n))
                        prev = candidate
                return res
                        
                        
                            
                        
                
                    
                
                
                
            
            