class Solution:
    def replaceWords(self, dictionary: List[str], A: str) -> str:
        dic = defaultdict(list)
        for word in dictionary:
            dic[word[0]].append(word)
            
        for key in dic:
            dic[key].sort(key = len)
        
        A = A.split()
        
        for i, a in enumerate(A):
            if a[0] in dic:
                lst = dic[a[0]]
                for word in lst:
                    if word == a[:len(word)]:
                        A[i] = word
                        break
        return " ".join(A)
                
                    
        
        